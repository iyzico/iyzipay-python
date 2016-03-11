import pprint
import unittest
import iyzipay


class CrossBookingSample(unittest.TestCase):
    def runTest(self):
        self.should_send_money_to_sub_merchant()
        self.should_receive_money_from_sub_merchant()

    def should_send_money_to_sub_merchant(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['subMerchantKey'] = 'sub merchant key'
        request['price'] = '1'
        request['reason'] = 'reason text'

        # make request
        cross_booking_to_sub_merchant = iyzipay.CrossBookingToSubMerchant()
        cross_booking_to_sub_merchant_response = cross_booking_to_sub_merchant.create(request, options)

        # print response
        pprint.pprint(cross_booking_to_sub_merchant_response.read().decode())

    def should_receive_money_from_sub_merchant(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['subMerchantKey'] = 'sub merchant key'
        request['price'] = '1'
        request['reason'] = 'reason text'

        # make request
        cross_booking_from_sub_merchant = iyzipay.CrossBookingFromSubMerchant()
        cross_booking_from_sub_merchant_response = cross_booking_from_sub_merchant.create(request, options)

        # print response
        pprint.pprint(cross_booking_from_sub_merchant_response.read().decode())
