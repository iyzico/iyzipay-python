import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.ConnectRefund import ConnectRefund


class ConnectRefundSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_refund_payment()

    def should_refund_payment(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'payment_transaction_id': '1',
                   'price': '1',
                   'ip': '127.0.0.1'}

        connect_refund = ConnectRefund.create(request, BaseSample.options)

        pprint.pprint(connect_refund)
