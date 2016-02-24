import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.ConnectCancel import ConnectCancel


class ConnectCancelSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_cancel_payment()

    def should_cancel_payment(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'payment_id': '1',
                   'ip': '127.0.0.1'}

        connect_cancel = ConnectCancel.create(request, BaseSample.options)

        pprint.pprint(connect_cancel)
