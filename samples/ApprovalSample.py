import pprint

from src.Iyzipay.Model.Approval import Approval


class ApprovalSample:
    def should_approve_payment_item(self):
        options = {'api_key': 'apiKey',
                   'secret_key': 'secretKey',
                   'base_url': 'https://stg.iyzipay.com'}

        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                    'payment_transaction_id': '2'}

        response = Approval.create(request, options)

        pprint.pprint(vars(response))
