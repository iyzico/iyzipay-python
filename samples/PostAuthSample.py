import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.PaymentPostAuth import PaymentPostAuth


class PostAuthSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_post_auth()

    def should_post_auth(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'payment_id': '1',
                   'ip': '127.0.0.1'}

        payment_post_auth = PaymentPostAuth.create(request, BaseSample.options)

        pprint.pprint(payment_post_auth)