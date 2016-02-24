import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.CheckoutFormAuth import CheckoutFormAuth
from src.Iyzipay.Model.CheckoutFormInitialize import CheckoutFormInitialize


class CheckoutFormSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_initialize_checkout_form()
        self.should_retrieve_checkout_form_auth()

    def should_initialize_checkout_form(self):
        buyer = {'id': '100',
                 'name': 'Hakan',
                 'surname': 'Erdoğan',
                 'identity_number': '16045258606',
                 'email': 'email@email.com',
                 'gsm_number': '05553456789',
                 'registration_date': '2011-02-17 12:00:00',
                 'last_login_date': '2015-04-20 12:00:00',
                 'registration_address': 'Maltepe',
                 'city': 'Istanbul',
                 'country': 'Turkiye',
                 'zip_code': '34840',
                 'ip': '192.168.123.102'}
        shipping_address = {'address': 'Malte Plaza No:56',
                            'zip_code': '34840',
                            'contact_name': 'Hakan',
                            'city': 'Istanbul',
                            'country': 'Turkiye'}
        billing_address = {'address': 'Malte Plaza No:56',
                           'zip_code': '34840',
                           'contact_name': 'Hakan',
                           'city': 'Istanbul',
                           'country': 'Turkiye'}
        basket_items = []
        item1 = {'id': 'BI101',
                 'name': 'Binocular',
                 'category1': 'Collectibles',
                 'category2': 'Accessories',
                 'item_type': 'PHYSICAL',
                 'price': '0.3',
                 'sub_merchant_key': 'sub merchant key',
                 'sub_merchant_price': '0.27'}
        basket_items.append(item1)
        item2 = {'id': 'BI102',
                 'name': 'Game code',
                 'category1': 'Game',
                 'category2': 'Online Game Items',
                 'item_type': 'VIRTUAL',
                 'price': '0.5',
                 'sub_merchant_key': 'sub merchant key',
                 'sub_merchant_price': '0.42'}
        basket_items.append(item2)
        item3 = {'id': 'BI103',
                 'name': 'Usb',
                 'category1': 'Electronics',
                 'category2': 'Usb / Cable',
                 'item_type': 'PHYSICAL',
                 'price': '0.2',
                 'sub_merchant_key': 'sub merchant key',
                 'sub_merchant_price': '0.18'}
        basket_items.append(item3)

        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'price': '1',
                   'basket_id': 'B67832',
                   'payment_group': 'PRODUCT',
                   'buyer': buyer,
                   'shipping_address': shipping_address,
                   'billing_address': billing_address,
                   'basket_items': basket_items,
                   'callback_url': 'https://www.merchant.com/callback',
                   'paid_price': '1.2'}
        checkout_form_initialize = CheckoutFormInitialize.create(request, BaseSample.options)

        pprint.pprint(checkout_form_initialize)

    def should_retrieve_checkout_form_auth(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'token' : 'token'}

        checkout_form_auth = CheckoutFormAuth.retrieve(request, BaseSample.options)

        pprint.pprint(checkout_form_auth)
