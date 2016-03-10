import pprint
import unittest
import iyzipay


class PaymentPostAuthSample(unittest.TestCase):
    def runTest(self):
        self.should_post_auth()

    def should_post_auth(self):

        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456'
        request['paymentId'] = '1'
        request['ip'] = '85.34.78.112'

        # make request
        payment_post_auth = iyzipay.PaymentPostAuth()
        payment_post_auth_response = payment_post_auth.create(request, options)

        # print response
        pprint.pprint(payment_post_auth_response.read().decode())
