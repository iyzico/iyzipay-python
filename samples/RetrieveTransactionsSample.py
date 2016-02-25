import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.BouncedBankTransferList import BouncedBankTransferList
from src.Iyzipay.Model.PayoutCompletedTransactionList import PayoutCompletedTransactionList


class RetrieveTransactionsSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_retrieve_payout_completed_transactions()
        self.should_retrieve_bounced_bank_transfers()

    def should_retrieve_payout_completed_transactions(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'date': '2016-01-22 19:13:00'}

        payout_completed_transaction_list = PayoutCompletedTransactionList.retrieve(request, BaseSample.options)

        pprint.pprint(payout_completed_transaction_list)

    def should_retrieve_bounced_bank_transfers(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'date': '2016-01-22 19:13:00'}

        bounced_bank_transfer_list = BouncedBankTransferList.retrieve(request, BaseSample.options)

        pprint.pprint(bounced_bank_transfer_list)