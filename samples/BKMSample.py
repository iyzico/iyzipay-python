import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.BKMInitialize import BKMInitialize


class BKMSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_initialize_bkm_express()

    def should_initialize_bkm_express(self):
        request = {'locale' : 'tr',
                   'conversation_id' : '123456789',
                   'price' : '1',
                   'basket_id' : 'B67832',
                   'payment_group' : 'product',
                   }
        buyer = {'id' : '100',
                 'name' : 'Hakan',
                 'surname' : 'Erdogan',
                 'identityNumber' : '16045258606',
                 'email' : 'email@email.com',
                 'gsmNumber' : '05553456789',
                 'registrationDate' : '2011-02-17 12:00:00',
                 'lastLoginDate' : '2015-04-20 12:00:00',
                 'registrationAddress' : 'Maltepe',
                 'city' : 'Istanbul',
                 'zipCode' : '34840',
                 'ip' : '192.168.123.102'}
        request['buyer'] = buyer
        shipping_address = {'address' : 'Malte Plaza No:56',
                            'zipCode' : '34840',
                            'contactName' : 'Hakan',
                            'city' : 'Istanbul',
                            'country' : 'Turkiye'}
        request['shipping_address'] = shipping_address
        billing_address = {'address' : 'Malte Plaza No:56',
                            'zipCode' : '34840',
                            'contactName' : 'Hakan',
                            'city' : 'Istanbul',
                            'country' : 'Turkiye'}
        request['billing_address'] = billing_address
        basket_items = []
        item1={}
        item1['id'] = "BI101"
        item1['name'] = "ABC Marka Kolye"
        item1['category1'] = "Giyim"
        item1['category2'] = "Aksesuar"
        item1['item_type'] = 'PHYSICAL'
        item1['price'] = "0.3"
        item1['sub_merchant_price'] = "0.27"
        item1['sub_merchant_key'] = "sub merchant key"
        basket_items.append(item1)

        item2 = {}
        item2['id'] = "BI102"
        item2['name'] = "XYZ Oyun Kodu"
        item2['category1'] = "Oyun"
        item2['category2'] = "Online Oyun Kodları"
        item2['item_type'] = 'VIRTUAL'
        item2['price'] = "0.5"
        item2['sub_merchant_price'] = "0.42"
        item2['sub_merchant_key'] = "sub merchant key"
        basket_items.append(item2)

        item3 = {}
        item3['id'] = "BI103"
        item3['name'] = "EDC Marka Usb"
        item3['category1'] = "Elektronik"
        item3['category2'] = "Usb / Cable"
        item3['item_type'] = 'PHYSICAL'
        item3['price'] = "0.2"
        item3['sub_merchant_price'] = "0.18"
        item3['sub_merchant_key'] = "sub merchant key"
        basket_items.append(item3)
        request['basket_items'] = basket_items
        request['callback_url'] = 'https://www.merchant.com/callbackUrl'

        bkm_initialize = BKMInitialize.create(request, BaseSample.options)

        pprint.pprint(bkm_initialize)

