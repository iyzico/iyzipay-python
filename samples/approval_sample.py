import pprint
import unittest
import iyzipay


class ApprovalSample(unittest.TestCase):
    def runTest(self):
        self.should_approve_payment_item()

    def should_approve_payment_item(self):

        options = {'base_url': iyzipay.base_url}
        options.update({'api_key': iyzipay.api_key})
        options.update({'secret_key': iyzipay.secret_key})

        request = {'locale': 'TR'}
        request.update({'conversationId': '123456'})
        request.update({'paymentTransactionId': '139'})

        approval = iyzipay.Approval()

        approval = approval.create(request, options)

        pprint.pprint(approval.read().decode())
