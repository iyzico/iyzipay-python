import pprint
import unittest
import iyzipay


class ApiTestSample(unittest.TestCase):
    def runTest(self):
        self.should_test_api()

    def should_test_api(self):

        options = dict([('base_url', iyzipay.base_url)])

        # make request
        api_test = iyzipay.ApiTest()
        api_test_response = api_test.retrieve(options)

        # print response
        pprint.pprint(api_test_response.read().decode())
