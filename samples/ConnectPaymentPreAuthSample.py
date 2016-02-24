import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.ConnectPaymentPreAuth import ConnectPaymentPreAuth


class ConnectPaymentPreAuthSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_pay_with_card()
        self.should_pay_with_card_token()

    def should_pay_with_card(self):
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
                   'payment_card': payment_card}

        connect_payment_pre_auth = ConnectPaymentPreAuth.create(request, BaseSample.options)

        pprint.pprint(connect_payment_pre_auth)

    def should_pay_with_card_token(self):
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
                   'payment_card': payment_card}

        connect_payment_pre_auth = ConnectPaymentPreAuth.create(request, BaseSample.options)

        pprint.pprint(connect_payment_pre_auth)