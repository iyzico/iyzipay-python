import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.ConnectThreeDSAuth import ConnectThreeDSAuth
from src.Iyzipay.Model.ConnectThreeDSInitialize import ConnectThreeDSInitialize


class ConnectThreeDSSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_initialize_threeds_with_card()
        self.should_initialize_threeds_with_card_token()
        self.should_auth_threeds()

    def should_initialize_threeds_with_card(self):
        payment_card = {'card_holder_name': 'John Doe',
                        'card_number': '5528790000000008',
                        'expire_month': '12',
                        'expire_year': '2030',
                        'cvc': '123',
                        'register_card': '0'}

        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'buyer_email': 'email@email.com',
                   'buyer_id': 'B2323',
                   'buyer_ip': '127.0.0.1',
                   'connector_name': 'connector name',
                   'installment': '1',
                   'paid_price': '1',
                   'price': '1',
                   'callback_url': 'https://www.merchant.com/callback',
                   'payment_card': payment_card}

        connect_threeds_initialize = ConnectThreeDSInitialize.create(request, BaseSample.options)

        pprint.pprint(connect_threeds_initialize)

    def should_initialize_threeds_with_card_token(self):
        payment_card = {'card_token': 'card token',
                        'card_user_key': 'card user key'}

        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'buyer_email': 'email@email.com',
                   'buyer_id': 'B2323',
                   'buyer_ip': '127.0.0.1',
                   'connector_name': 'connector name',
                   'installment': '1',
                   'paid_price': '1',
                   'price': '1',
                   'callback_url': 'https://www.merchant.com/callback',
                   'payment_card': payment_card}

        connect_threeds_initialize = ConnectThreeDSInitialize.create(request, BaseSample.options)

        pprint.pprint(connect_threeds_initialize)

    def should_auth_threeds(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'payment_id': '1',
                   'conversation_data': ''}

        connect_threeds_auth = ConnectThreeDSAuth.create(request, BaseSample.options)

        pprint.pprint(connect_threeds_auth)
