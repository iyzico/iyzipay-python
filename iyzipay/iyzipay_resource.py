import random
import string
import base64
import hashlib
import http.client


class IyzipayResource:

    def __init__(self):
        pass

    RANDOM_STRING_SIZE = 8

    @staticmethod
    def get_http_header(options=None, pki_string=None):
        header = {"Accept": "application/json", "Content-type": "application/json"}
        if pki_string is not None:
            random_header_value = "".join(
                random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in
                range(IyzipayResource.RANDOM_STRING_SIZE))
            header.update(
                {'Authorization': IyzipayResource.prepare_authorization_string(options, random_header_value, pki_string)})
            header.update({'x-iyzi-rnd': random_header_value})
        return header

    @staticmethod
    def get_plain_http_header(options):
        return IyzipayResource.get_http_header(None, options)

    @staticmethod
    def prepare_authorization_string(options, random_header_value, pki_string):
        hashed = IyzipayResource.generate_hash(options['api_key'], options['secret_key'], random_header_value, pki_string)
        return IyzipayResource.format_header_string(options['api_key'], hashed)

    @staticmethod
    def generate_hash(api_key, secret_key, random_string, pki_string):
        hash_str = api_key + random_string + secret_key + pki_string
        hex_dig = hashlib.sha1(hash_str.encode()).digest()
        return base64.b64encode(hex_dig)

    @staticmethod
    def format_header_string(api_key, hashed):
        hashed = hashed.decode('utf-8')
        return 'IYZWS %s:%s' % (api_key, hashed)


class ApiTest(IyzipayResource):

    @staticmethod
    def retrieve(options):
        connection = http.client.HTTPSConnection(options['base_url'])
        connection.request('GET', '/payment/test', None, IyzipayResource.get_http_header(options))
        return connection.getresponse()


