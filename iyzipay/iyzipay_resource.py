import base64
import hashlib
import hmac
import importlib
import json
import random
import string
from urllib.parse import urlencode

import iyzipay


class IyzipayResource:
    RANDOM_STRING_SIZE = 8
    header = {
        "Accept": "application/json",
        "Content-type": "application/json",
        'x-iyzi-client-version': 'iyzipay-python-1.0.46'
    }

    def __init__(self):
        self.httplib = importlib.import_module('http.client')

    def verify_signature(self, params, secret_key, signature):
        calculated_signature = self.calculate_hmac_sha256_signature(params, secret_key)
        verified = signature == calculated_signature
        print('Signature verified:', verified)

    def connect(self, method, url, options, request_body_dict=None):
        connection = self.httplib.HTTPSConnection(options['base_url'])
        body_str = json.dumps(request_body_dict)
        header = self.get_http_header(url, options, body_str)
        connection.request(method, url, body_str, header)
        return connection.getresponse()

    def get_http_header(self, url, options=None, body_str=None):
        random_str = self.generate_random_string(self.RANDOM_STRING_SIZE)
        self.header.update({'x-iyzi-rnd': random_str})
        return self.get_http_header_v2(url, options, random_str, body_str)

    def get_http_header_v2(self, url, options, random_str, body_str):
        url = url.split('?')[0]
        hashed_v2_str = self.generate_v2_hash(options['api_key'], url, options['secret_key'], random_str, body_str)
        self.header.update({'Authorization': 'IYZWSv2 %s' % hashed_v2_str})
        return self.header

    @staticmethod
    def strip_zero(number):
        has_zero = number.endswith('.0')
        return number.replace('.0', '') if has_zero else number

    @staticmethod
    def calculate_hmac_sha256_signature(params, secret_key):
        secret_key = bytes(secret_key.encode('utf-8'))
        msg = ':'.join(params).encode('utf-8')

        hmac_obj = hmac.new(secret_key, digestmod=hashlib.sha256)
        hmac_obj.update(msg)
        return hmac_obj.hexdigest()

    @staticmethod
    def generate_v2_hash(api_key, url, secret_key, random_str, body_str):
        secret_key = bytes(secret_key.encode('utf-8'))
        msg = (random_str + url + body_str).encode('utf-8')

        hmac_obj = hmac.new(secret_key, digestmod=hashlib.sha256)
        hmac_obj.update(msg)
        signature = hmac_obj.hexdigest()
        authorization_params = [
            'apiKey:' + api_key,
            'randomKey:' + random_str,
            'signature:' + signature
        ]
        return base64.b64encode('&'.join(authorization_params).encode()).decode()

    @staticmethod
    def generate_random_string(size):
        return "".join(
            random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in
            range(size))

    @staticmethod
    def resource_pki(request):
        return 'locale=' + request.get('locale') + (
            ',conversationId=' + request.get('conversationId') + ',' if request.get('conversationId') else ',')

    @staticmethod
    def payment_card_pki(payment_card):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append('cardHolderName', payment_card.get('cardHolderName'))
        pki_builder.append('cardNumber', payment_card.get('cardNumber'))
        pki_builder.append('expireYear', payment_card.get('expireYear'))
        pki_builder.append('expireMonth', payment_card.get('expireMonth'))
        pki_builder.append('cvc', payment_card.get('cvc'))
        pki_builder.append('registerCard', payment_card.get('registerCard'))
        pki_builder.append('cardAlias', payment_card.get('cardAlias'))
        pki_builder.append('cardToken', payment_card.get('cardToken'))
        pki_builder.append('cardUserKey', payment_card.get('cardUserKey'))
        return pki_builder.get_request_string()


class ApiTest(IyzipayResource):
    def retrieve(self, options):
        return self.connect('GET', '/payment/test', options)


class BinNumber(IyzipayResource):
    def retrieve(self, request, options):
        return self.connect('POST', '/payment/bin/check', options, request)


class InstallmentInfo(IyzipayResource):
    def retrieve(self, request, options):
        return self.connect('POST', '/payment/iyzipos/installment', options, request)


class Approval(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/iyzipos/item/approve', options, request)


class Disapproval(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/iyzipos/item/disapprove', options, request)


class CheckoutFormInitialize(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/iyzipos/checkoutform/initialize/ecom', options, request)


class CheckoutForm(IyzipayResource):
    def retrieve(self, request, options):
        return self.connect('POST', '/payment/iyzipos/checkoutform/auth/ecom/detail', options, request)


class Payment(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/auth', options, request)

    def retrieve(self, request, options):
        return self.connect('POST', '/payment/detail', options, request)

    def refund(self, request, options):
        return self.connect('POST', '/v2/payment/refund', options, request)


class ThreedsInitialize(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/3dsecure/initialize', options, request)


class ThreedsPayment(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/3dsecure/auth', options, request)

    def retrieve(self, request, options):
        return self.connect('POST', '/payment/detail', options, request)


class ThreedsV2Payment(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/v2/3dsecure/auth', options, request)


class Cancel(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/cancel', options, request)


class Refund(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/refund', options, request)


class Card(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/cardstorage/card', options, request)

    def delete(self, request, options):
        return self.connect('DELETE', '/cardstorage/card', options, request)


class CardList(IyzipayResource):
    def retrieve(self, request, options):
        return self.connect('POST', '/cardstorage/cards', options, request)


class Bkm(IyzipayResource):
    def retrieve(self, request, options):
        return self.connect('POST', '/payment/bkm/auth/detail', options, request)


class BkmInitialize(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/bkm/initialize', options, request)


class PeccoInitialize(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/pecco/initialize', options, request)


class PeccoPayment(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/pecco/auth', options, request)


class CheckoutFormInitializePreAuth(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/iyzipos/checkoutform/initialize/preauth/ecom', options, request)


class PaymentPreAuth(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/preauth', options, request)

    def retrieve(self, request, options):
        return self.connect('POST', '/payment/detail', options, request)


class PaymentPostAuth(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/postauth', options, request)


class ThreedsInitializePreAuth(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/3dsecure/initialize/preauth', options, request)


class RefundChargedFromMerchant(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/iyzipos/refund/merchant/charge', options, request)


class PayoutCompletedTransactionList(IyzipayResource):
    def retrieve(self, request, options):
        return self.connect('POST', '/reporting/settlement/payoutcompleted', options, request)


class BouncedBankTransferList(IyzipayResource):
    def retrieve(self, request, options):
        return self.connect('POST', '/reporting/settlement/bounced', options, request)


class SubMerchant(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/onboarding/submerchant', options, request)

    def update(self, request, options):
        return self.connect('PUT', '/onboarding/submerchant', options, request)

    def update_item(self, request, options):
        return self.connect('PUT', '/payment/item', options, request)

    def retrieve(self, request, options):
        return self.connect('POST', '/onboarding/submerchant/detail', options, request)


class CrossBookingToSubMerchant(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/crossbooking/send', options, request)


class CrossBookingFromSubMerchant(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/crossbooking/receive', options, request)


class BasicPayment(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/auth/basic', options, request)


class BasicPaymentPreAuth(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/preauth/basic', options, request)


class BasicPaymentPostAuth(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/postauth/basic', options, request)


class BasicThreedsInitialize(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/3dsecure/initialize/basic', options, request)


class BasicThreedsInitializePreAuth(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/iyziconnect/initialize3ds/preauth', options, request)


class BasicThreedsPayment(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/3dsecure/auth/basic', options, request)


class BasicBkm(IyzipayResource):
    def retrieve(self, request, options):
        return self.connect('POST', '/payment/bkm/auth/detail/basic', options, request)


class BasicBkmInitialize(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/bkm/initialize/basic', options, request)


class RetrievePaymentDetails(IyzipayResource):
    def retrieve(self, request, options):
        payment_id = str(request.get('paymentId'))
        payment_conversation_id = str(request.get('paymentConversationId'))
        param_name = 'paymentId' if payment_id else 'paymentConversationId'
        param_value = payment_id if payment_id else payment_conversation_id
        param = param_name + '=' + param_value
        return self.connect('GET', '/v2/reporting/payment/details?' + param, options)


class RetrieveTransactions(IyzipayResource):
    def retrieve(self, request, options):
        page = str(request.get('page'))
        transaction_date = str(request.get('transactionDate'))
        query_params = 'transactionDate=' + transaction_date + '&page=' + page
        return self.connect('GET', '/v2/reporting/payment/transactions?' + query_params, options)


class ReportingScrollTransaction(IyzipayResource):
    def retrieve(self, request, options):
        transaction_date = request.get('transactionDate')
        document_scrolling_vo_sort_order = request.get('documentScrollVoSortingOrder')
        last_id = request.get('lastId')
        conversation_id = request.get('conversationId')
        params = 'transactionDate=' + transaction_date + '&documentScrollVoSortingOrder=' + document_scrolling_vo_sort_order + '&lastId=' + last_id + '&conversationId=' + conversation_id
        return self.connect('GET', '/v2/reporting/payment/scroll-transactions?' + params, options)


class IyziFileBase64Encoder:
    @staticmethod
    def encode(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')


class IyziLinkProduct(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/v2/iyzilink/products', options, request)

    def fast_link(self, request, options):
        locale = str(request.get('locale', 'tr'))
        return self.connect('POST', '/v2/iyzilink/fast-link/products?locale=' + locale, options, request)

    def retrieve(self, request, options):
        if request.get('token') is None:
            raise Exception('token must be in request')
        token = str(request.get('token'))
        return self.connect('GET', '/v2/iyzilink/products/' + token, options)

    def get(self, request, options):
        page = str(request.get('page') or 1)
        count = str(request.get('count') or 10)
        return self.connect('GET', '/v2/iyzilink/products/?page=' + page + '&count=' + count, options)

    def update(self, request, options):
        if request.get('token') is None:
            raise Exception('token must be in request')
        token = str(request.get('token'))
        return self.connect('PUT', '/v2/iyzilink/products/' + token, options, request)

    def update_product_status(self, request, options):
        if request.get('token') is None:
            raise Exception('token must be in request')
        token = str(request.get('token'))
        if request.get('status') is None:
            raise Exception('status must be in request')
        status = str(request.get('status'))
        return self.connect('PATCH', '/v2/iyzilink/products/' + token + '/status/' + status, options)

    def delete(self, request, options):
        if request.get('token') is None:
            raise Exception('token must be in request')
        token = str(request.get('token'))
        return self.connect('DELETE', '/v2/iyzilink/products/' + token, options)


class RetrieveLoyalty(IyzipayResource):
    def retrieve(self, request, options):
        return self.connect('POST', '/payment/loyalty/inquire', options, request)

    def to_pki_string_create(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentCard', self.payment_card_pki(request.get('paymentCard')))
        pki_builder.append('currency', request.get('currency'))
        return pki_builder.get_request_string()


class PayWithIyzico(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/payment/pay-with-iyzico/initialize', options, request)


class SubscriptionProduct(IyzipayResource):
    url = '/v2/subscription/products'

    def create(self, request, options):
        return self.connect('POST', self.url, options, request)

    def list(self, options):
        return self.connect('GET', self.url, options)

    def retrieve(self, request, options):
        product_reference_code = str(request.get('product_reference_code'))
        return self.connect('GET', self.url + '/' + product_reference_code, options)

    def delete(self, request, options):
        product_reference_code = str(request.get('product_reference_code'))
        return self.connect('DELETE', self.url + '/' + product_reference_code, options)

    def update(self, request, options):
        product_reference_code = str(request.get('product_reference_code'))
        return self.connect('POST', self.url + '/' + product_reference_code, options, request)


class SubscriptionPricingPlan(IyzipayResource):
    product_url = '/v2/subscription/products/'
    pricing_plan_url = '/v2/subscription/pricing-plans/'

    def create(self, request, options):
        product_reference_code = str(request.get('product_reference_code'))
        return self.connect('POST', self.product_url + product_reference_code + '/pricing-plans', options, request)

    def list(self, request, options):
        product_reference_code = str(request.get('product_reference_code'))
        return self.connect('GET', self.product_url + product_reference_code + '/pricing-plans', options)

    def update(self, request, options):
        pricing_plan_reference_code = str(request.get('pricing_plan_reference_code'))
        return self.connect('POST', self.pricing_plan_url + pricing_plan_reference_code, options, request)

    def retrieve(self, request, options):
        pricing_plan_reference_code = str(request.get('pricing_plan_reference_code'))
        return self.connect('GET', self.pricing_plan_url + pricing_plan_reference_code, options)

    def delete(self, request, options):
        pricing_plan_reference_code = str(request.get('pricing_plan_reference_code'))
        return self.connect('DELETE', self.pricing_plan_url + pricing_plan_reference_code, options)


class SubscriptionCheckoutForm(IyzipayResource):
    url = '/v2/subscription/checkoutform'

    def create(self, request, options):
        return self.connect('POST', self.url + '/initialize', options, request)

    def retrieve(self, request, options):
        token = str(request.get('token'))
        return self.connect('GET', self.url + '/' + token, options, request)


class Subscription(IyzipayResource):
    url = '/v2/subscription'

    def retrieve(self, options):
        return self.connect('GET', self.url + '/subscriptions', options)

    def initialize(self, request, options):
        return self.connect('POST', self.url + '/initialize', options, request)

    def initialize_with_customer(self, request, options):
        return self.connect('POST', self.url + '/initialize/with-customer', options, request)

    def list(self, request, options):
        query = urlencode({k: v for k, v in (request or {}).items() if v is not None}, doseq=True)
        list_url = self.url + '/subscriptions'
        if query:
            list_url += '?' + query
        return self.connect('GET', list_url, options)

    def activate(self, request, options):
        subscription_reference_code = str(request.get('referenceCode'))
        activate_url = '/subscriptions/' + subscription_reference_code + '/activate'
        return self.connect('POST', self.url + activate_url, options, request)

    def retry(self, request, options):
        return self.connect('POST', self.url + '/operation/retry', options, request)

    def cancel(self, request, options):
        subscription_reference_code = str(request.get('subscriptionReferenceCode'))
        cancel_url = '/subscriptions/' + subscription_reference_code + '/cancel'
        return self.connect('POST', self.url + cancel_url, options, request)

    def upgrade(self, request, options):
        subscription_reference_code = str(request.get('subscriptionReferenceCode'))
        upgrade_url = '/subscriptions/' + subscription_reference_code + '/upgrade'
        return self.connect('POST', self.url + upgrade_url, options, request)


class SubscriptionCardUpdate(IyzipayResource):
    url = "/v2/subscription/card-update/checkoutform/initialize"

    def initialize(self, request, options):
        return self.connect('POST', self.url, options, request)

    def initialize_with_subscription(self, request, options):
        return self.connect('POST', self.url + '/with-subscription', options, request)


class SubscriptionCustomer(IyzipayResource):
    url = "/v2/subscription/customers"

    def create(self, request, options):
        return self.connect('POST', self.url, options, request)

    def update(self, request, options):
        customer_reference_code = str(request.get('customerReferenceCode'))
        return self.connect('POST', self.url + '/' + customer_reference_code, options, request)

    def retrieve(self, request, options):
        customer_reference_code = str(request.get('customerReferenceCode'))
        return self.connect('GET', self.url + '/' + customer_reference_code, options)

    def delete(self, request, options):
        customer_reference_code = str(request.get('customerReferenceCode'))
        return self.connect('POST', self.url + '/delete/' + customer_reference_code, options)

    def list(self, request, options):
        query = urlencode({k: v for k, v in (request or {}).items() if v is not None}, doseq=True)
        list_url = self.url
        if query:
            list_url += '?' + query
        return self.connect('GET', list_url, options)
