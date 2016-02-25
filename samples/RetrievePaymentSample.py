import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.Payment import Payment


class RetrievePaymentSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_retrieve_payment()

    def should_retrieve_payment(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'payment_id': '1',
                   'payment_conversation_id': '123456789'}

        payment = Payment.retrieve(request, BaseSample.options)

        pprint.pprint(payment)