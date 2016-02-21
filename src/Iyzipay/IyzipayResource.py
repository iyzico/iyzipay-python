import random
import string


from src.Iyzipay.HashGenerator import HashGenerator


class IyzipayResource:
    RANDOM_STRING_SIZE = 8

    @staticmethod
    def get_http_header(request, options=None, authorize_request=True):
        header = {'Accept': 'application/json'}
        header.update({'Content-type': 'application/json'})
        if authorize_request is True:
            random_header_value = "".join(
                random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in
                range(IyzipayResource.RANDOM_STRING_SIZE))
            header.update(
                {'Authorization': IyzipayResource.prepare_authorization_string(request, options, random_header_value)})
            header.update({'x-iyzi-rnd': random_header_value})
        return header

    @staticmethod
    def get_plain_http_header(options):
        return IyzipayResource.get_http_header(None, options, False)

    @staticmethod
    def prepare_authorization_string(request, options, random_header_value):
        hashed = HashGenerator.generate_hash(options['api_key'], options['secret_key'], random_header_value, request)
        return IyzipayResource.format_header_string(options['api_key'], hashed)

    @staticmethod
    def format_header_string(api_key, hashed):
        hashed = hashed.decode('utf-8')
        return 'IYZWS %s:%s' % (api_key, hashed)

    def json_decode_and_prepare_response(self, response, raw_result):
        json_result = raw_result.json()
        response.raw_result = raw_result
        response.from_json(json_result)

    @classmethod
    def get_json_object(cls, request):
        from src.Iyzipay.JsonBuilder import JsonBuilder
        return JsonBuilder.create() \
            .add('locale', request['locale']) \
            .add('conversationId', request['conversation_id']) \
            .get_object()

    @classmethod
    def to_pki_request_string(cls, request):
        from src.Iyzipay.RequestStringBuilder import RequestStringBuilder
        return RequestStringBuilder.create() \
                    .append('locale', request['locale']) \
                    .append('conversationId', request['conversation_id']) \
                    .get_request_string()


