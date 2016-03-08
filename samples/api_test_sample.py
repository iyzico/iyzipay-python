import pprint
import unittest
import iyzipay


class ApiTestSample(unittest.TestCase):
    def runTest(self):
        self.should_test_api()

    def should_test_api(self):

        options = {'base_url': iyzipay.base_url}
        api_test = iyzipay.ApiTest()
        api_test = api_test.retrieve(options)

        pprint.pprint(api_test.read().decode())
