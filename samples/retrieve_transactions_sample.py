import pprint
import unittest
import iyzipay


class RetrieveTransactionsSample(unittest.TestCase):
    def runTest(self):
        self.should_retrieve_payout_completed_transactions()
        self.should_retrieve_bounced_bank_transfers()

    def should_retrieve_payout_completed_transactions(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['date'] = '2016-01-22 19:13:00'

        # make request
        payout_completed_transactions_list = iyzipay.PayoutCompletedTransactionList()
        payout_completed_transactions_list_response = payout_completed_transactions_list.retrieve(request, options)

        # print response
        pprint.pprint(payout_completed_transactions_list_response.read().decode())

    def should_retrieve_bounced_bank_transfers(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['date'] = '2016-01-22 19:13:00'

        # make request
        bounced_bank_transfer_list = iyzipay.BouncedBankTransferList()
        bounced_bank_transfer_list_response = bounced_bank_transfer_list.retrieve(request, options)

        # print response
        pprint.pprint(bounced_bank_transfer_list_response.read().decode())
