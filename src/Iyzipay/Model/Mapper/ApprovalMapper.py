from src.Iyzipay.Model.Mapper.IyzipayResourceMapper import IyzipayResourceMapper


class ApprovalMapper(IyzipayResourceMapper):
    @staticmethod
    def new_instance():
        return ApprovalMapper()

    def map_response(self, response, json_result):
        super().map_response(response, json_result)
        if 'paymentTransactionId' in json_result.keys():
            response['payment_transaction_id'] = json_result['paymentTransactionsId']
        return response