import pprint
import unittest
import iyzipay


class RefundSample(unittest.TestCase):
    def runTest(self):
        self.should_refund()
        self.should_refund_charged_from_merchant()

    def should_refund(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['paymentTransactionId'] = '1'
        request['price'] = '0.1'
        request['ip'] = '85.34.78.112'

        # make request
        refund = iyzipay.Refund()
        refund_response = refund.create(request, options)

        # print response
        pprint.pprint(refund_response.read().decode())

    def should_refund_charged_from_merchant(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['paymentTransactionId'] = '1'
        request['price'] = '0.1'
        request['ip'] = '85.34.78.112'

        # make request
        refund_charged_from_merchant = iyzipay.RefundChargedFromMerchant()
        refund_charged_from_merchant_response = refund_charged_from_merchant.create(request, options)

        # print response
        pprint.pprint(refund_charged_from_merchant_response.read().decode())
