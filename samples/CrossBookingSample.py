import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.CrossBookingFromSubMerchant import CrossBookingFromSubMerchant
from src.Iyzipay.Model.CrossBookingToSubMerchant import CrossBookingToSubMerchant


class CrossBookingSample(BaseSample, unittest.TestCase):
    def runTest(self):
        # self.should_send_money_to_sub_merchant()
        self.should_receive_money_from_sub_merchant()

    def should_send_money_to_sub_merchant(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'sub_merchant_key': 'sub merchant key',
                   'price': '1',
                   'reason': 'reason text'}

        cross_booking_to_sub_merchant = CrossBookingToSubMerchant.create(request, BaseSample.options)

        pprint.pprint(cross_booking_to_sub_merchant)

    def should_receive_money_from_sub_merchant(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'sub_merchant_key': 'sub merchant key',
                   'price': '1',
                   'reason': 'reason text'}

        cross_booking_from_sub_merchant = CrossBookingFromSubMerchant.create(request, BaseSample.options)

        pprint.pprint(cross_booking_from_sub_merchant)
