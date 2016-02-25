import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.Refund import Refund
from src.Iyzipay.Model.RefundChargedFromMertchant import RefundChargedFromMertchant


class RefundSample(BaseSample, unittest.TestCase):
    def runTest(self):
        # self.should_refund()
        self.should_refund_charged_from_merchant()

    def should_refund(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'payment_transaction_id': '1',
                   'price': '0.1',
                   'ip': '127.0.0.1'}

        refund = Refund.create(request, BaseSample.options)

        pprint.pprint(refund)

    def should_refund_charged_from_merchant(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'payment_transaction_id': '1',
                   'price': '0.1',
                   'ip': '127.0.0.1'}
        refund_charged_from_merchant = RefundChargedFromMertchant.create(request, BaseSample.options)

        pprint.pprint(refund_charged_from_merchant)
