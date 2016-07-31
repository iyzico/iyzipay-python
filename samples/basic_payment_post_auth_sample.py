# coding=utf-8
import unittest
import iyzipay


class BasicPaymentPostAuthSample(unittest.TestCase):
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
        request['currency'] = 'TRY'

        # make request
        basic_payment_post_auth = iyzipay.BasicPaymentPostAuth()
        basic_payment_post_auth_response = basic_payment_post_auth.create(request, options)

        # print response
        print(basic_payment_post_auth_response.read().decode('utf-8'))

