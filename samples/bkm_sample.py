import pprint
import unittest
import iyzipay
import base64


class BKMSample(unittest.TestCase):
    def runTest(self):
        self.should_initialize_bkm()
        self.should_retrieve_bkm_auth()

    def should_initialize_bkm(self):

        options = {'base_url': iyzipay.base_url}
        options.update({'api_key': iyzipay.api_key})
        options.update({'secret_key': iyzipay.secret_key})

        request = {'locale': 'TR'}
        request.update({'conversationId': '123456'})
        request.update({'price': '1.0'})
        request.update({'basketId': 'B67832'})
        request.update({'paymentGroup': 'PRODUCT'})
        request.update({'callbackUrl': 'https://www.merchant.com/callbackUrl'})

        buyer = {'id': '100'}
        buyer.update({'name': 'John'})
        buyer.update({'surname': 'Doe'})
        buyer.update({'identityNumber': '16045258606'})
        buyer.update({'email': 'doe@doe.com'})
        buyer.update({'gsmNumber': '05553456789'})
        buyer.update({'registrationDate': '2011-02-17 12:00:00'})
        buyer.update({'lastLoginDate': '2015-04-20 12:00:00'})
        buyer.update({'registrationAddress': 'Maltepe'})
        buyer.update({'city': 'Istanbul'})
        buyer.update({'country': 'Türkiye'})
        buyer.update({'zipCode': '34840'})
        buyer.update({'ip': '192.168.123.102'})
        request['buyer'] = buyer

        address = {'address': 'Maltepe Plaza No:56'}
        address.update({'zipCode': '34840'})
        address.update({'contactName': 'Hakan'})
        address.update({'city': 'Istanbul'})
        address.update({'country': 'Türkiye'})
        request['shippingAddress'] = address
        request['billingAddress'] = address

        basket_items = []
        basket_item = {'id': 'BI101'}
        basket_item.update({'name': 'XYZ Oyun Kodu'})
        basket_item.update({'category1': 'Oyun'})
        basket_item.update({'category2': 'Online Oyun Kodlari'})
        basket_item.update({'itemType': 'VIRTUAL'})
        basket_item.update({'price': '1.0'})
        basket_item.update({'subMerchantKey': 'subMerchantKey'})
        basket_item.update({'subMerchantPrice': '0.9'})
        basket_items.append(basket_item)

        request['basketItems'] = basket_items

        bkm_initialize = iyzipay.BKMInitialize()

        bkm_initialize = bkm_initialize.create(request, options)

        pprint.pprint(bkm_initialize.read().decode())

    def should_retrieve_bkm_auth(self):

        options = {'base_url': iyzipay.base_url}
        options.update({'api_key': iyzipay.api_key})
        options.update({'secret_key': iyzipay.secret_key})

        request = {'locale': 'TR'}
        request.update({'conversationId': '123456'})
        request.update({'token': 'mockToken1453382198111'})

        bkm_auth = iyzipay.BKMAuth()

        bkm_auth = bkm_auth.retrieve(request, options)

        pprint.pprint(bkm_auth.read().decode())
