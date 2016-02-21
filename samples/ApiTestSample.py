import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.ApiTest import ApiTest


class ApiTestSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_test_api()

    def should_test_api(self):
        api_test = ApiTest.retrieve(BaseSample.options)

        pprint.pprint(api_test)
