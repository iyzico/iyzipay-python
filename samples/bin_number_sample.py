import pprint
import unittest
import iyzipay


class BinNumberSample(unittest.TestCase):
    def runTest(self):
        self.should_retrieve_bin_number()

    def should_retrieve_bin_number(self):

        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['binNumber'] = '454671'

        # make request
        bin_number = iyzipay.BinNumber()
        bin_number_response = bin_number.retrieve(request, options)

        # print response
        pprint.pprint(bin_number_response.read().decode())
