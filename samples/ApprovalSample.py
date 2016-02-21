import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.Approval import Approval
from src.Iyzipay.Model.Disapproval import Disapproval


class ApprovalSample(BaseSample, unittest.TestCase):

    def runTest(self):
        self.should_approve_payment_item()
        self.should_disapprove_payment_item()

    def should_approve_payment_item(cls):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                    'payment_transaction_id': '2'}

        response = Approval.create(request, BaseSample.options)

        pprint.pprint(response)

    def should_disapprove_payment_item(cls):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'payment_transaction_id': '2'}

        response = Disapproval.create(request, BaseSample.options)

        pprint.pprint(response)
