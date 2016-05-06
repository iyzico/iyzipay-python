import pprint
import unittest
import iyzipay


class ApprovalSample(unittest.TestCase):
    def runTest(self):
        self.should_approve_payment_item()
        self.should_disapprove_payment_item()

    def should_approve_payment_item(self):

        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['paymentTransactionId'] = '1'

        # make request
        approval = iyzipay.Approval()
        approval_response = approval.create(request, options)

        # print response
        pprint.pprint(approval_response.read().decode())

    def should_disapprove_payment_item(self):

        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['paymentTransactionId'] = '1'

        # make request
        disapproval = iyzipay.Disapproval()
        disapproval_response = disapproval.create(request, options)

        # print response
        pprint.pprint(disapproval_response.read().decode())