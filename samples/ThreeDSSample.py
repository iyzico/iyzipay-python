import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.ThreeDSAuth import ThreeDSAuth
from src.Iyzipay.Model.ThreeDSInitialize import ThreeDSInitialize


class ThreeDSSample(BaseSample, unittest.TestCase):
    def runTest(self):
        # self.should_initialize_threeds_payment_with_physical_and_virtual_item_for_market_place()
        # self.should_initialize_threeds_payment_with_physical_and_virtual_item_for_listing_or_subscription()
        self.should_auth_threeds()

    def should_initialize_threeds_payment_with_physical_and_virtual_item_for_market_place(self):
        buyer = {'id': 'BY789',
                 'name': 'John',
                 'surname': 'Doe',
                 'gsm_number': '+905350000000',
                 'email': 'email@email.com',
                 'identity_number': '16045258606',
                 'registration_date': '2011-02-17 12:00:00',
                 'last_login_date': '2015-04-20 12:00:00',
                 'registration_address': 'Maltepe',
                 'city': 'Istanbul',
                 'country': 'Turkiye',
                 'zip_code': '34840',
                 'ip': '192.168.123.102'}

        payment_card = {'card_holder_name': 'John Doe',
                        'card_number': '5528790000000008',
                        'expire_month': '12',
                        'expire_year': '2030',
                        'cvc': '123',
                        'register_card': '0'}

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
                   'paid_price': '1.1',
                   'installment': '1',
                   'basket_id': 'B67832',
                   'payment_channel': 'WEB',
                   'payment_group': 'PRODUCT',
                   'callback_url': 'https://www.merchant.com/callback',
                   'payment_card': payment_card,
                   'buyer': buyer,
                   'shipping_address': shipping_address,
                   'billing_address': billing_address,
                   'basket_items': basket_items}

        three_ds_initialize = ThreeDSInitialize.create(request, BaseSample.options)
        pprint.pprint(three_ds_initialize)

    def should_initialize_threeds_payment_with_physical_and_virtual_item_for_listing_or_subscription(self):
        buyer = {'id': 'BY789',
                 'name': 'John',
                 'surname': 'Doe',
                 'gsm_number': '+905350000000',
                 'email': 'email@email.com',
                 'identity_number': '16045258606',
                 'registration_date': '2011-02-17 12:00:00',
                 'last_login_date': '2015-04-20 12:00:00',
                 'registration_address': 'Maltepe',
                 'city': 'Istanbul',
                 'country': 'Turkiye',
                 'zip_code': '34840',
                 'ip': '192.168.123.102'}

        payment_card = {'card_holder_name': 'John Doe',
                        'card_number': '5528790000000008',
                        'expire_month': '12',
                        'expire_year': '2030',
                        'cvc': '123',
                        'register_card': '0'}

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
                 'item_type': 'VIRTUAL',
                 'price': '0.3',}
        basket_items.append(item1)
        item2 = {'id': 'BI102',
                 'name': 'Game code',
                 'category1': 'Game',
                 'category2': 'Online Game Items',
                 'item_type': 'VIRTUAL',
                 'price': '0.5',}
        basket_items.append(item2)
        item3 = {'id': 'BI103',
                 'name': 'Usb',
                 'category1': 'Electronics',
                 'category2': 'Usb / Cable',
                 'item_type': 'PHYSICAL',
                 'price': '0.2',}
        basket_items.append(item3)

        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'price': '1',
                   'paid_price': '1.1',
                   'installment': '1',
                   'basket_id': 'B67832',
                   'payment_channel': 'WEB',
                   'payment_group': 'LISTING',
                   'callback_url': 'https://www.merchant.com/callback',
                   'payment_card': payment_card,
                   'buyer': buyer,
                   'shipping_address': shipping_address,
                   'billing_address': billing_address,
                   'basket_items': basket_items}

        three_ds_initialize = ThreeDSInitialize.create(request, BaseSample.options)
        pprint.pprint(three_ds_initialize)

    def should_auth_threeds(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'payment_id': '1',
                   'conversation_data': 'conversation data'}

        three_ds_auth = ThreeDSAuth.create(request, BaseSample.options)

        pprint.pprint(three_ds_auth)


