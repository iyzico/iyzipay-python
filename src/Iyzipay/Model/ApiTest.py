from src.Iyzipay.HttpClient import HttpClient
from src.Iyzipay.IyzipayResource import IyzipayResource


class ApiTest(IyzipayResource):
    @staticmethod
    def retrieve(options):
        return HttpClient.create().get(options['base_url'] + "/payment/test", IyzipayResource.get_plain_http_header(options)).json()
