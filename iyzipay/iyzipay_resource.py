import base64
import hashlib
import hmac
import importlib
import json
import random
import re
import string

import iyzipay


class IyzipayResource:
    RANDOM_STRING_SIZE = 8
    RE_SEARCH_V2 = r'/v2/'
    header = {
        "Accept": "application/json", 
        "Content-type": "application/json",
        'x-iyzi-client-version': 'iyzipay-python-1.1'
    }

    def __init__(self):
        self.httplib = importlib.import_module('http.client')

    def connect(self, method, url, options, request_body_dict=None, pki=None):
        connection = self.httplib.HTTPSConnection(options['base_url'])
        body_str = json.dumps(request_body_dict)
        header = self.get_http_header(url, options, body_str, pki)
        connection.request(method, url, body_str, header)
        return connection.getresponse()

    def get_http_header(self, url, options=None, body_str=None, pki_string=None):
        random_str = self.generate_random_string(self.RANDOM_STRING_SIZE)
        self.header.update({'x-iyzi-rnd': random_str})
        if re.search(self.RE_SEARCH_V2, url, re.IGNORECASE) is not None:
            return self.get_http_header_v2(url, options, random_str, body_str)
        else:
            return self.get_http_header_v1(options, pki_string, random_str)

    def get_http_header_v1(self, options, pki_string, random_str=None):
        if pki_string is not None:
            self.header.update(
                {'Authorization': self.prepare_auth_string(options, random_str, pki_string)})
        return self.header

    def get_http_header_v2(self, url, options, random_str, body_str):
        url = url.split('?')[0]
        hashed_v2_str = self.generate_v2_hash(options['api_key'], url, options['secret_key'], random_str, body_str)
        self.header.update({'Authorization': 'IYZWSv2 %s' % hashed_v2_str})
        return self.header

    def generate_v2_hash(self, api_key, url, secret_key, random_str, body_str):
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

    def get_plain_http_header(self, options):
        return self.get_http_header_v1(None, options)

    def prepare_auth_string(self, options, random_str, pki_string):
        hashed = self.generate_hash(options['api_key'], options['secret_key'], random_str, pki_string)
        return self.format_header_string(options['api_key'], hashed)

    def generate_random_string(self, size):
        return "".join(
                random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in
                range(size))

    @staticmethod
    def generate_hash(api_key, secret_key, random_string, pki_string):
        hash_str = api_key + random_string + secret_key + pki_string
        hex_dig = hashlib.sha1(hash_str.encode()).digest()

        return base64.b64encode(hex_dig)

    @staticmethod
    def format_header_string(api_key, hashed):
        hashed = hashed.decode('utf-8')
        return 'IYZWS %s:%s' % (api_key, hashed)

    @staticmethod
    def resource_pki(request):
        return 'locale=' + request.get('locale') + (',conversationId=' + request.get('conversationId') + ',' if request.get('conversationId') else ',')

    @staticmethod
    def buyer_pki(buyer):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append('id', buyer.get('id'))
        pki_builder.append('name', buyer.get('name'))
        pki_builder.append('surname', buyer.get('surname'))
        pki_builder.append('identityNumber', buyer.get('identityNumber'))
        pki_builder.append('email', buyer.get('email'))
        pki_builder.append('gsmNumber', buyer.get('gsmNumber'))
        pki_builder.append('registrationDate', buyer.get('registrationDate'))
        pki_builder.append('lastLoginDate', buyer.get('lastLoginDate'))
        pki_builder.append('registrationAddress', buyer.get('registrationAddress'))
        pki_builder.append('city', buyer.get('city'))
        pki_builder.append('country', buyer.get('country'))
        pki_builder.append('zipCode', buyer.get('zipCode'))
        pki_builder.append('ip', buyer.get('ip'))
        return pki_builder.get_request_string()

    @staticmethod
    def address_pki(address):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append('address', address.get('address'))
        pki_builder.append('zipCode', address.get('zipCode'))
        pki_builder.append('contactName', address.get('contactName'))
        pki_builder.append('city', address.get('city'))
        pki_builder.append('country', address.get('country'))
        return pki_builder.get_request_string()

    @staticmethod
    def basket_pki(basket_items):
        basket_items_pki = []
        for item in basket_items:
            pki_builder = iyzipay.PKIBuilder('')
            pki_builder.append('id', item.get('id'))
            pki_builder.append_price('price', item.get('price'))
            pki_builder.append('name', item.get('name'))
            pki_builder.append('category1', item.get('category1'))
            pki_builder.append('category2', item.get('category2'))
            pki_builder.append('itemType', item.get('itemType'))
            pki_builder.append('subMerchantKey', item.get('subMerchantKey'))
            pki_builder.append_price('subMerchantPrice', item.get('subMerchantPrice'))
            basket_items_pki.append(pki_builder.get_request_string())
        return basket_items_pki

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

    @staticmethod
    def installment_details_pki(installment_details):
        installments_pki = []
        for item in installment_details:
            pki_builder = iyzipay.PKIBuilder('')
            pki_builder.append('bankId', item.get('bankId'))
            pki_builder.append_array('installmentPrices',
                                     IyzipayResource.installment_prices_pki(item.get('installmentPrices')))
            installments_pki.append(pki_builder.get_request_string())
        return installments_pki

    @staticmethod
    def installment_prices_pki(installment_prices):
        installments_pki = []
        for item in installment_prices:
            pki_builder = iyzipay.PKIBuilder('')
            pki_builder.append('installmentNumber', item.get('installmentNumber'))
            pki_builder.append_price('totalPrice', item.get('totalPrice'))
            installments_pki.append(pki_builder.get_request_string())
        return installments_pki

    @staticmethod
    def card_pki(card):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append('cardAlias', card.get('cardAlias'))
        pki_builder.append('cardNumber', card.get('cardNumber'))
        pki_builder.append('expireYear', card.get('expireYear'))
        pki_builder.append('expireMonth', card.get('expireMonth'))
        pki_builder.append('cardHolderName', card.get('cardHolderName'))
        return pki_builder.get_request_string()


class ApiTest(IyzipayResource):
    def retrieve(self, options):
        return self.connect('GET', '/payment/test', options)


class BinNumber(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/bin/check', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('binNumber', request.get('binNumber'))
        return pki_builder.get_request_string()


class InstallmentInfo(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/installment', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('binNumber', request.get('binNumber'))
        pki_builder.append_price('price', request.get('price'))
        return pki_builder.get_request_string()


class Approval(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/item/approve', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentTransactionId', request.get('paymentTransactionId'))
        return pki_builder.get_request_string()


class Disapproval(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/item/disapprove', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentTransactionId', request.get('paymentTransactionId'))
        return pki_builder.get_request_string()


class CheckoutFormInitialize(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/checkoutform/initialize/ecom', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append('basketId', request.get('basketId'))
        pki_builder.append('paymentGroup', request.get('paymentGroup'))
        pki_builder.append('buyer', self.buyer_pki(request.get('buyer')))
        pki_builder.append('shippingAddress', self.address_pki(request.get('shippingAddress')))
        pki_builder.append('billingAddress', self.address_pki(request.get('billingAddress')))
        pki_builder.append_array('basketItems', self.basket_pki(request.get('basketItems')))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        pki_builder.append('paymentSource', request.get('paymentSource'))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('posOrderId', request.get('posOrderId'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('forceThreeDS', request.get('forceThreeDS'))
        pki_builder.append('cardUserKey', request.get('cardUserKey'))
        pki_builder.append_array('enabledInstallments', request.get('enabledInstallments'))
        pki_builder.append('debitCardAllowed', request.get('debitCardAllowed'))
        return pki_builder.get_request_string()


class CheckoutForm(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/checkoutform/auth/ecom/detail', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('token', request.get('token'))
        return pki_builder.get_request_string()


class Payment(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string_create(request)
        return self.connect('POST', '/payment/auth', options, request, pki)

    def retrieve(self, request, options):
        pki = self.to_pki_string_retrieve(request)
        return self.connect('POST', '/payment/detail', options, request, pki)

    def to_pki_string_create(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('installment', request.get('installment'))
        pki_builder.append('paymentChannel', request.get('paymentChannel'))
        pki_builder.append('basketId', request.get('basketId'))
        pki_builder.append('paymentGroup', request.get('paymentGroup'))
        pki_builder.append('paymentCard', self.payment_card_pki(request.get('paymentCard')))
        pki_builder.append('buyer', self.buyer_pki(request.get('buyer')))
        pki_builder.append('shippingAddress', self.address_pki(request.get('shippingAddress')))
        pki_builder.append('billingAddress', self.address_pki(request.get('billingAddress')))
        pki_builder.append_array('basketItems', self.basket_pki(request.get('basketItems')))
        pki_builder.append('paymentSource', request.get('paymentSource'))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('posOrderId', request.get('posOrderId'))
        pki_builder.append('connectorName', request.get('connectorName'))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        return pki_builder.get_request_string()

    def to_pki_string_retrieve(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentId', request.get('paymentId'))
        pki_builder.append('paymentConversationId', request.get('paymentConversationId'))
        return pki_builder.get_request_string()


class ThreedsInitialize(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/3dsecure/initialize', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('installment', request.get('installment'))
        pki_builder.append('paymentChannel', request.get('paymentChannel'))
        pki_builder.append('basketId', request.get('basketId'))
        pki_builder.append('paymentGroup', request.get('paymentGroup'))
        pki_builder.append('paymentCard', self.payment_card_pki(request.get('paymentCard')))
        pki_builder.append('buyer', self.buyer_pki(request.get('buyer')))
        pki_builder.append('shippingAddress', self.address_pki(request.get('shippingAddress')))
        pki_builder.append('billingAddress', self.address_pki(request.get('billingAddress')))
        pki_builder.append_array('basketItems', self.basket_pki(request.get('basketItems')))
        pki_builder.append('paymentSource', request.get('paymentSource'))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        return pki_builder.get_request_string()


class ThreedsPayment(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string_create(request)
        return self.connect('POST', '/payment/3dsecure/auth', options, request, pki)

    def retrieve(self, request, options):
        pki = self.to_pki_string_retrieve(request)
        return self.connect('POST', '/payment/detail', options, request, pki)

    def to_pki_string_create(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentId', request.get('paymentId'))
        pki_builder.append('conversationData', request.get('conversationData'))
        return pki_builder.get_request_string()

    def to_pki_string_retrieve(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentId', request.get('paymentId'))
        pki_builder.append('paymentConversationId', request.get('paymentConversationId'))
        return pki_builder.get_request_string()


class Cancel(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/cancel', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentId', request.get('paymentId'))
        pki_builder.append('ip', request.get('ip'))
        pki_builder.append('reason', request.get('reason'))
        pki_builder.append('description', request.get('description'))
        return pki_builder.get_request_string()


class Refund(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/refund', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentTransactionId', request.get('paymentTransactionId'))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append('ip', request.get('ip'))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('reason', request.get('reason'))
        pki_builder.append('description', request.get('description'))
        return pki_builder.get_request_string()


class Card(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string_create(request)
        return self.connect('POST', '/cardstorage/card', options, request, pki)

    def delete(self, request, options):
        pki = self.to_pki_string_delete(request)
        return self.connect('DELETE', '/cardstorage/card', options, request, pki)

    def to_pki_string_create(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('externalId', request.get('externalId'))
        pki_builder.append('email', request.get('email'))
        pki_builder.append('cardUserKey', request.get('cardUserKey'))
        pki_builder.append('card', self.card_pki(request.get('card')))
        return pki_builder.get_request_string()

    def to_pki_string_delete(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('cardUserKey', request.get('cardUserKey'))
        pki_builder.append('cardToken', request.get('cardToken'))
        return pki_builder.get_request_string()


class CardList(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/cardstorage/cards', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('cardUserKey', request.get('cardUserKey'))
        return pki_builder.get_request_string()


class Bkm(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/bkm/auth/detail', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('token', request.get('token'))
        return pki_builder.get_request_string()


class BkmInitialize(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/bkm/initialize', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append('basketId', request.get('basketId'))
        pki_builder.append('paymentGroup', request.get('paymentGroup'))
        pki_builder.append('buyer', self.buyer_pki(request.get('buyer')))
        pki_builder.append('shippingAddress', self.address_pki(request.get('shippingAddress')))
        pki_builder.append('billingAddress', self.address_pki(request.get('billingAddress')))
        pki_builder.append_array('basketItems', self.basket_pki(request.get('basketItems')))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        pki_builder.append('paymentSource', request.get('paymentSource'))
        pki_builder.append_array('enabledInstallments', request.get('enabledInstallments'))
        return pki_builder.get_request_string()


class PeccoInitialize(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/pecco/initialize', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append('basketId', request.get('basketId'))
        pki_builder.append('paymentGroup', request.get('paymentGroup'))
        pki_builder.append('buyer', self.buyer_pki(request.get('buyer')))
        pki_builder.append('shippingAddress', self.address_pki(request.get('shippingAddress')))
        pki_builder.append('billingAddress', self.address_pki(request.get('billingAddress')))
        pki_builder.append_array('basketItems', self.basket_pki(request.get('basketItems')))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        pki_builder.append('paymentSource', request.get('paymentSource'))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        return pki_builder.get_request_string()


class PeccoPayment(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/pecco/auth', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('token', request.get('token'))
        return pki_builder.get_request_string()


class CheckoutFormInitializePreAuth(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/checkoutform/initialize/preauth/ecom', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append('basketId', request.get('basketId'))
        pki_builder.append('paymentGroup', request.get('paymentGroup'))
        pki_builder.append('buyer', self.buyer_pki(request.get('buyer')))
        pki_builder.append('shippingAddress', self.address_pki(request.get('shippingAddress')))
        pki_builder.append('billingAddress', self.address_pki(request.get('billingAddress')))
        pki_builder.append_array('basketItems', self.basket_pki(request.get('basketItems')))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        pki_builder.append('paymentSource', request.get('paymentSource'))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('posOrderId', request.get('posOrderId'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('forceThreeDS', request.get('forceThreeDS'))
        pki_builder.append('cardUserKey', request.get('cardUserKey'))
        pki_builder.append_array('enabledInstallments', request.get('enabledInstallments'))
        return pki_builder.get_request_string()


class PaymentPreAuth(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string_create(request)
        return self.connect('POST', '/payment/preauth', options, request, pki)

    def retrieve(self, request, options):
        pki = self.to_pki_string_retrieve(request)
        return self.connect('POST', '/payment/detail', options, request, pki)

    def to_pki_string_create(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('installment', request.get('installment'))
        pki_builder.append('paymentChannel', request.get('paymentChannel'))
        pki_builder.append('basketId', request.get('basketId'))
        pki_builder.append('paymentGroup', request.get('paymentGroup'))
        pki_builder.append('paymentCard', self.payment_card_pki(request.get('paymentCard')))
        pki_builder.append('buyer', self.buyer_pki(request.get('buyer')))
        pki_builder.append('shippingAddress', self.address_pki(request.get('shippingAddress')))
        pki_builder.append('billingAddress', self.address_pki(request.get('billingAddress')))
        pki_builder.append_array('basketItems', self.basket_pki(request.get('basketItems')))
        pki_builder.append('paymentSource', request.get('paymentSource'))
        pki_builder.append('currency', request.get('currency'))
        return pki_builder.get_request_string()

    def to_pki_string_retrieve(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentId', request.get('paymentId'))
        pki_builder.append('paymentConversationId', request.get('paymentConversationId'))
        return pki_builder.get_request_string()


class PaymentPostAuth(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string_create(request)
        return self.connect('POST', '/payment/postauth', options, request, pki)

    def to_pki_string_create(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentId', request.get('paymentId'))
        pki_builder.append('ip', request.get('ip'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('currency', request.get('currency'))
        return pki_builder.get_request_string()


class ThreedsInitializePreAuth(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/3dsecure/initialize/preauth', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('installment', request.get('installment'))
        pki_builder.append('paymentChannel', request.get('paymentChannel'))
        pki_builder.append('basketId', request.get('basketId'))
        pki_builder.append('paymentGroup', request.get('paymentGroup'))
        pki_builder.append('paymentCard', self.payment_card_pki(request.get('paymentCard')))
        pki_builder.append('buyer', self.buyer_pki(request.get('buyer')))
        pki_builder.append('shippingAddress', self.address_pki(request.get('shippingAddress')))
        pki_builder.append('billingAddress', self.address_pki(request.get('billingAddress')))
        pki_builder.append_array('basketItems', self.basket_pki(request.get('basketItems')))
        pki_builder.append('paymentSource', request.get('paymentSource'))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        return pki_builder.get_request_string()


class RefundChargedFromMerchant(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/refund/merchant/charge', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentTransactionId', request.get('paymentTransactionId'))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append('ip', request.get('ip'))
        pki_builder.append('currency', request.get('currency'))
        return pki_builder.get_request_string()


class PayoutCompletedTransactionList(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/reporting/settlement/payoutcompleted', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('date', request.get('date'))
        return pki_builder.get_request_string()


class BouncedBankTransferList(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/reporting/settlement/bounced', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('date', request.get('date'))
        return pki_builder.get_request_string()


class SubMerchant(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string_create(request)
        return self.connect('POST', '/onboarding/submerchant', options, request, pki)

    def update(self, request, options):
        pki = self.to_pki_string_update(request)
        return self.connect('PUT', '/onboarding/submerchant', options, request, pki)

    def retrieve(self, request, options):
        pki = self.to_pki_string_retrieve(request)
        return self.connect('POST', '/onboarding/submerchant/detail', options, request, pki)

    def to_pki_string_create(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('name', request.get('name'))
        pki_builder.append('email', request.get('email'))
        pki_builder.append('gsmNumber', request.get('gsmNumber'))
        pki_builder.append('address', request.get('address'))
        pki_builder.append('iban', request.get('iban'))
        pki_builder.append('taxOffice', request.get('taxOffice'))
        pki_builder.append('contactName', request.get('contactName'))
        pki_builder.append('contactSurname', request.get('contactSurname'))
        pki_builder.append('legalCompanyTitle', request.get('legalCompanyTitle'))
        pki_builder.append('swiftCode', request.get('swiftCode'))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('subMerchantExternalId', request.get('subMerchantExternalId'))
        pki_builder.append('identityNumber', request.get('identityNumber'))
        pki_builder.append('taxNumber', request.get('taxNumber'))
        pki_builder.append('subMerchantType', request.get('subMerchantType'))
        return pki_builder.get_request_string()

    def to_pki_string_update(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('name', request.get('name'))
        pki_builder.append('email', request.get('email'))
        pki_builder.append('gsmNumber', request.get('gsmNumber'))
        pki_builder.append('address', request.get('address'))
        pki_builder.append('iban', request.get('iban'))
        pki_builder.append('taxOffice', request.get('taxOffice'))
        pki_builder.append('contactName', request.get('contactName'))
        pki_builder.append('contactSurname', request.get('contactSurname'))
        pki_builder.append('legalCompanyTitle', request.get('legalCompanyTitle'))
        pki_builder.append('swiftCode', request.get('swiftCode'))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('subMerchantKey', request.get('subMerchantKey'))
        pki_builder.append('identityNumber', request.get('identityNumber'))
        pki_builder.append('taxNumber', request.get('taxNumber'))
        return pki_builder.get_request_string()

    def to_pki_string_retrieve(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('subMerchantExternalId', request.get('subMerchantExternalId'))
        return pki_builder.get_request_string()


class CrossBookingToSubMerchant(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/crossbooking/send', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('subMerchantKey', request.get('subMerchantKey'))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append('reason', request.get('reason'))
        pki_builder.append('currency', request.get('currency'))
        return pki_builder.get_request_string()


class CrossBookingFromSubMerchant(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/crossbooking/receive', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('subMerchantKey', request.get('subMerchantKey'))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append('reason', request.get('reason'))
        pki_builder.append('currency', request.get('currency'))
        return pki_builder.get_request_string()


class BasicPayment(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/auth/basic', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('installment', request.get('installment'))
        pki_builder.append('buyerEmail', request.get('buyerEmail'))
        pki_builder.append('buyerId', request.get('buyerId'))
        pki_builder.append('buyerIp', request.get('buyerIp'))
        pki_builder.append('posOrderId', request.get('posOrderId'))
        pki_builder.append('paymentCard', self.payment_card_pki(request.get('paymentCard')))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('connectorName', request.get('connectorName'))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        return pki_builder.get_request_string()


class BasicPaymentPreAuth(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/preauth/basic', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('installment', request.get('installment'))
        pki_builder.append('buyerEmail', request.get('buyerEmail'))
        pki_builder.append('buyerId', request.get('buyerId'))
        pki_builder.append('buyerIp', request.get('buyerIp'))
        pki_builder.append('posOrderId', request.get('posOrderId'))
        pki_builder.append('paymentCard', self.payment_card_pki(request.get('paymentCard')))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('connectorName', request.get('connectorName'))
        return pki_builder.get_request_string()


class BasicPaymentPostAuth(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string_create(request)
        return self.connect('POST', '/payment/postauth/basic', options, request, pki)

    def to_pki_string_create(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentId', request.get('paymentId'))
        pki_builder.append('ip', request.get('ip'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('currency', request.get('currency'))
        return pki_builder.get_request_string()


class BasicThreedsInitialize(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/3dsecure/initialize/basic', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('installment', request.get('installment'))
        pki_builder.append('buyerEmail', request.get('buyerEmail'))
        pki_builder.append('buyerId', request.get('buyerId'))
        pki_builder.append('buyerIp', request.get('buyerIp'))
        pki_builder.append('posOrderId', request.get('posOrderId'))
        pki_builder.append('paymentCard', self.payment_card_pki(request.get('paymentCard')))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('connectorName', request.get('connectorName'))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        return pki_builder.get_request_string()


class BasicThreedsInitializePreAuth(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyziconnect/initialize3ds/preauth', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append_price('paidPrice', request.get('paidPrice'))
        pki_builder.append('installment', request.get('installment'))
        pki_builder.append('buyerEmail', request.get('buyerEmail'))
        pki_builder.append('buyerId', request.get('buyerId'))
        pki_builder.append('buyerIp', request.get('buyerIp'))
        pki_builder.append('posOrderId', request.get('posOrderId'))
        pki_builder.append('paymentCard', self.payment_card_pki(request.get('paymentCard')))
        pki_builder.append('currency', request.get('currency'))
        pki_builder.append('connectorName', request.get('connectorName'))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        return pki_builder.get_request_string()


class BasicThreedsPayment(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/3dsecure/auth/basic', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentId', request.get('paymentId'))
        pki_builder.append('conversationData', request.get('conversationData'))
        return pki_builder.get_request_string()


class BasicBkm(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/bkm/auth/detail/basic', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('token', request.get('token'))
        return pki_builder.get_request_string()


class BasicBkmInitialize(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/bkm/initialize/basic', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('connectorName', request.get('connectorName'))
        pki_builder.append_price('price', request.get('price'))
        pki_builder.append('callbackUrl', request.get('callbackUrl'))
        pki_builder.append('buyerEmail', request.get('buyerEmail'))
        pki_builder.append('buyerId', request.get('buyerId'))
        pki_builder.append('buyerIp', request.get('buyerIp'))
        pki_builder.append('posOrderId', request.get('posOrderId'))
        pki_builder.append_array('installmentDetails', self.installment_details_pki(request.get('installmentDetails')))
        return pki_builder.get_request_string()


class RetrievePaymentDetails(IyzipayResource):
    def retrieve(self, request, options):
        payment_conversation_id = str(request.get('paymentConversationId'))
        return self.connect('GET', '/v2/reporting/payment/details?paymentConversationId=' + payment_conversation_id, options)


class RetrieveTransactions(IyzipayResource):
    def retrieve(self, request, options):
        page = str(request.get('page'))
        transaction_date = str(request.get('transactionDate'))
        query_params = 'transactionDate=' + transaction_date + '&page=' + page
        return self.connect('GET', '/v2/reporting/payment/transactions?' + query_params, options)


class IyziFileBase64Encoder:
    @staticmethod
    def encode(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')


class IyziLinkProduct(IyzipayResource):
    def create(self, request, options):
        return self.connect('POST', '/v2/iyzilink/products/', options, request)
    
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
    
    def delete(self, request, options):
        if request.get('token') is None:
            raise Exception('token must be in request')
        token = str(request.get('token'))
        return self.connect('DELETE', '/v2/iyzilink/products/' + token, options)
