from src.Iyzipay.HttpClient import HttpClient
from src.Iyzipay.IyzipayResource import IyzipayResource
from src.Iyzipay.Model.Mapper.ApprovalMapper import ApprovalMapper


class Approval(IyzipayResource):

    @classmethod
    def create(cls, request, options):

        raw_result = HttpClient.create().post(options['base_url'] + "/payment/iyzipos/item/approve",
                                              IyzipayResource.get_http_header(request, options), request)
        ApprovalMapper.new_instance().map_response({}, raw_result)
    @classmethod
    def request_to_string(cls, request):
        pass
