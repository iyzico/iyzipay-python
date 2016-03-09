import random
import string
import base64
import hashlib
import http.client
import json
import iyzipay


class IyzipayResource:
    def __init__(self):
        pass

    RANDOM_STRING_SIZE = 8

    def connect(self, method, url, options, request=None, pki=None):
        connection = http.client.HTTPSConnection(options['base_url'])
        request_json = json.dumps(request)
        connection.request(method, url, request_json, self.get_http_header(options, pki))
        return connection.getresponse()

    def get_http_header(self, options=None, pki_string=None):
        header = {"Accept": "application/json", "Content-type": "application/json"}
        if pki_string is not None:
            random_header_value = "".join(
                random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in
                range(self.RANDOM_STRING_SIZE))
            header.update(
                {'Authorization': self.prepare_auth_string(options, random_header_value, pki_string)})
            header.update({'x-iyzi-rnd': random_header_value})
        return header

    def get_plain_http_header(self, options):
        return self.get_http_header(None, options)

    def prepare_auth_string(self, options, random_str, pki_string):
        hashed = self.generate_hash(options['api_key'], options['secret_key'], random_str, pki_string)
        return self.format_header_string(options['api_key'], hashed)

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
        return 'locale=' + request['locale'] + ',conversationId=' + request['conversationId'] + ','

    @staticmethod
    def buyer_pki(buyer):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append('id', buyer['id'])
        pki_builder.append('name', buyer['name'])
        pki_builder.append('surname', buyer['surname'])
        pki_builder.append('identityNumber', buyer['identityNumber'])
        pki_builder.append('email', buyer['email'])
        pki_builder.append('gsmNumber', buyer['gsmNumber'])
        pki_builder.append('registrationDate', buyer['registrationDate'])
        pki_builder.append('lastLoginDate', buyer['lastLoginDate'])
        pki_builder.append('registrationAddress', buyer['registrationAddress'])
        pki_builder.append('city', buyer['city'])
        pki_builder.append('country', buyer['country'])
        pki_builder.append('zipCode', buyer['zipCode'])
        pki_builder.append('ip', buyer['ip'])
        return pki_builder.get_request_string()

    @staticmethod
    def address_pki(address):
        pki_builder = iyzipay.PKIBuilder('')
        pki_builder.append('address', address['address'])
        pki_builder.append('zipCode', address['zipCode'])
        pki_builder.append('contactName', address['contactName'])
        pki_builder.append('city', address['city'])
        pki_builder.append('country', address['country'])
        return pki_builder.get_request_string()

    @staticmethod
    def basket_pki(basket_items):
        basket_items_pki = []
        for item in basket_items:
            pki_builder = iyzipay.PKIBuilder('')
            pki_builder.append('id', item['id'])
            pki_builder.append_price('price', item['price'])
            pki_builder.append('name', item['name'])
            pki_builder.append('category1', item['category1'])
            pki_builder.append('category2', item['category2'])
            pki_builder.append('itemType', item['itemType'])
            pki_builder.append('subMerchantKey', item['subMerchantKey'])
            pki_builder.append_price('subMerchantPrice', item['subMerchantPrice'])
            basket_items_pki.append(pki_builder.get_request_string())
        return basket_items_pki


class ApiTest(IyzipayResource):
    def retrieve(self, options):
        return self.connect('GET', '/payment/test', options)


class BinNumber(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/bin/check', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('binNumber', request['binNumber'])
        return pki_builder.get_request_string()


class Approval(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/item/approve', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentTransactionId', request['paymentTransactionId'])
        return pki_builder.get_request_string()


class BKMAuth(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/bkm/auth/ecom/detail', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('token', request['token'])
        return pki_builder.get_request_string()


class BKMInitialize(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/bkm/initialize/ecom', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request['price'])
        pki_builder.append('basketId', request['basketId'])
        pki_builder.append('paymentGroup', request['paymentGroup'])
        pki_builder.append('buyer', self.buyer_pki(request['buyer']))
        pki_builder.append('shippingAddress', self.address_pki(request['shippingAddress']))
        pki_builder.append('billingAddress', self.address_pki(request['billingAddress']))
        pki_builder.append_array('basketItems', self.basket_pki(request['basketItems']))
        pki_builder.append('callbackUrl', request['callbackUrl'])
        return pki_builder.get_request_string()


class Cancel(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/cancel', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('paymentId', request['paymentId'])
        pki_builder.append('ip', request['ip'])
        return pki_builder.get_request_string()


class CheckoutFormInitialize(IyzipayResource):
    def create(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/checkoutform/initialize/ecom', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append_price('price', request['price'])
        pki_builder.append('basketId', request['basketId'])
        pki_builder.append('paymentGroup', request['paymentGroup'])
        pki_builder.append('buyer', self.buyer_pki(request['buyer']))
        pki_builder.append('shippingAddress', self.address_pki(request['shippingAddress']))
        pki_builder.append('billingAddress', self.address_pki(request['billingAddress']))
        pki_builder.append_array('basketItems', self.basket_pki(request['basketItems']))
        pki_builder.append('callbackUrl', request['callbackUrl'])
        if 'paymentSource' in request:
            pki_builder.append('paymentSource', request['paymentSource'])
        if 'posOrderId' in request:
            pki_builder.append('posOrderId', request['posOrderId'])
        pki_builder.append_price('paidPrice', request['paidPrice'])
        if 'forceThreeDS' in request:
            pki_builder.append('forceThreeDS', request['forceThreeDS'])
        if 'cardUserKey' in request:
            pki_builder.append('cardUserKey', request['cardUserKey'])
        return pki_builder.get_request_string()


class CheckoutFormAuth(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/checkoutform/auth/ecom/detail', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        pki_builder.append('token', request['token'])
        return pki_builder.get_request_string()


class InstallmentInfo(IyzipayResource):
    def retrieve(self, request, options):
        pki = self.to_pki_string(request)
        return self.connect('POST', '/payment/iyzipos/installment', options, request, pki)

    def to_pki_string(self, request):
        pki_builder = iyzipay.PKIBuilder(self.resource_pki(request))
        if 'binNumber' in request:
            pki_builder.append('binNumber', request['binNumber'])
        pki_builder.append_price('price', request['price'])
        return pki_builder.get_request_string()