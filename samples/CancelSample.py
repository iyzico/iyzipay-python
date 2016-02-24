import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.Cancel import Cancel


class CancelSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_cancel_payment()

    def should_cancel_payment(self):
        request = {'locale' : 'tr',
                   'conversation_id' : '123456789',
                   'payment_id' : '1',
                   'ip' : '127.0.0.1'
                   }
        cancel = Cancel.create(request, BaseSample.options)

        pprint.pprint(cancel)
