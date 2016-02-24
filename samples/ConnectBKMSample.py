import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.ConnectBKMAuth import ConnectBKMAuth
from src.Iyzipay.Model.ConnectBKMInitialize import ConnectBKMInitialize


class ConnectBKMSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.shoul_initialize_bkm_express()
        self.should_retrieve_bkm_auth()

    def shoul_initialize_bkm_express(self):
        installment_details = [self.isbank_installment_details(),
                               self.finansbank_installment_details(),
                               self.akbank_installment_details(),
                               self.ykb_installment_details(),
                               self.denizbank_installment_details(),
                               self.halkbank_installment_details()]
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'price': '1',
                   'callback_url': 'https://www.merchant.com/callback',
                   'buyer_id': '100',
                   'buyer_email': 'email@email.com',
                   'buyer_ip': '198.168.123.102',
                   'connector_name': 'connector name',
                   'installment_details': installment_details}
        connect_bkm_auth = ConnectBKMInitialize.create(request, BaseSample.options)
        pprint.pprint(connect_bkm_auth)

    def should_retrieve_bkm_auth(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'token': 'token'}

        connect_bkm_auth = ConnectBKMAuth.retrieve(request, BaseSample.options)

        pprint.pprint(connect_bkm_auth)

    def isbank_installment_details(self):
        installment_prices = []
        single_installment = {'installment_number': '1',
                              'total_price': '1'}
        two_installments = {'installment_number': '2',
                            'total_price': '1.1'}
        three_installments = {'installment_number': '3',
                              'total_price': '1.1'}
        six_installments = {'installment_number': '6',
                            'total_price': '1.2'}
        nine_installments = {'installment_number': '9',
                             'total_price': '1.4'}
        installment_prices.append(single_installment)
        installment_prices.append(two_installments)
        installment_prices.append(three_installments)
        installment_prices.append(six_installments)
        installment_prices.append(nine_installments)

        installment_detail = {'bank_id': '64',
                              'installment_prices': installment_prices}
        return installment_detail

    def finansbank_installment_details(self):
        installment_prices = []
        single_installment = {'installment_number': '1',
                              'total_price': '1'}
        two_installments = {'installment_number': '2',
                            'total_price': '1.1'}
        three_installments = {'installment_number': '3',
                              'total_price': '1.1'}
        six_installments = {'installment_number': '6',
                            'total_price': '1.2'}
        nine_installments = {'installment_number': '9',
                             'total_price': '1.4'}
        installment_prices.append(single_installment)
        installment_prices.append(two_installments)
        installment_prices.append(three_installments)
        installment_prices.append(six_installments)
        installment_prices.append(nine_installments)

        installment_detail = {'bank_id': '111',
                              'installment_prices': installment_prices}
        return installment_detail

    def akbank_installment_details(self):
        installment_prices = []
        single_installment = {'installment_number': '1',
                              'total_price': '1'}
        two_installments = {'installment_number': '2',
                            'total_price': '1.1'}
        three_installments = {'installment_number': '3',
                              'total_price': '1.1'}
        six_installments = {'installment_number': '6',
                            'total_price': '1.2'}
        nine_installments = {'installment_number': '9',
                             'total_price': '1.4'}
        installment_prices.append(single_installment)
        installment_prices.append(two_installments)
        installment_prices.append(three_installments)
        installment_prices.append(six_installments)
        installment_prices.append(nine_installments)

        installment_detail = {'bank_id': '46',
                              'installment_prices': installment_prices}
        return installment_detail

    def ykb_installment_details(self):
        installment_prices = []
        single_installment = {'installment_number': '1',
                              'total_price': '1'}
        two_installments = {'installment_number': '2',
                            'total_price': '1.1'}
        three_installments = {'installment_number': '3',
                              'total_price': '1.1'}
        six_installments = {'installment_number': '6',
                            'total_price': '1.2'}
        nine_installments = {'installment_number': '9',
                             'total_price': '1.4'}
        installment_prices.append(single_installment)
        installment_prices.append(two_installments)
        installment_prices.append(three_installments)
        installment_prices.append(six_installments)
        installment_prices.append(nine_installments)

        installment_detail = {'bank_id': '67',
                              'installment_prices': installment_prices}
        return installment_detail

    def denizbank_installment_details(self):
        installment_prices = []
        single_installment = {'installment_number': '1',
                              'total_price': '1'}
        two_installments = {'installment_number': '2',
                            'total_price': '1.1'}
        three_installments = {'installment_number': '3',
                              'total_price': '1.1'}
        six_installments = {'installment_number': '6',
                            'total_price': '1.2'}
        nine_installments = {'installment_number': '9',
                             'total_price': '1.4'}
        installment_prices.append(single_installment)
        installment_prices.append(two_installments)
        installment_prices.append(three_installments)
        installment_prices.append(six_installments)
        installment_prices.append(nine_installments)

        installment_detail = {'bank_id': '134',
                              'installment_prices': installment_prices}
        return installment_detail

    def halkbank_installment_details(self):
        installment_prices = []
        single_installment = {'installment_number': '1',
                              'total_price': '1'}
        two_installments = {'installment_number': '2',
                            'total_price': '1.1'}
        three_installments = {'installment_number': '3',
                              'total_price': '1.1'}
        six_installments = {'installment_number': '6',
                            'total_price': '1.2'}
        nine_installments = {'installment_number': '9',
                             'total_price': '1.4'}
        installment_prices.append(single_installment)
        installment_prices.append(two_installments)
        installment_prices.append(three_installments)
        installment_prices.append(six_installments)
        installment_prices.append(nine_installments)

        installment_detail = {'bank_id': '12',
                              'installment_prices': installment_prices}
        return installment_detail


