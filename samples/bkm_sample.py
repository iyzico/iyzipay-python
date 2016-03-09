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

        request = {'locale': 'tr'}
        request.update({'conversationId': '123456789'})
        request.update({'price': '1'})
        request.update({'basketId': 'B67832'})
        request.update({'paymentGroup': 'PRODUCT'})
        request.update({'callbackUrl': 'https://www.merchant.com/callback'})

        buyer = {'id': 'BY789'}
        buyer.update({'name': 'John'})
        buyer.update({'surname': 'Doe'})
        buyer.update({'gsmNumber': '+905350000000'})
        buyer.update({'email': 'email@email.com'})
        buyer.update({'identityNumber': '74300864791'})
        buyer.update({'lastLoginDate': '2015-10-05 12:43:35'})
        buyer.update({'registrationDate': '2013-04-21 15:12:09'})
        buyer.update({'registrationAddress': 'Address'})
        buyer.update({'ip': '85.34.78.112'})
        buyer.update({'city': 'Istanbul'})
        buyer.update({'country': 'Turkey'})
        buyer.update({'zipCode': '34732'})
        request['buyer'] = buyer

        address = {'address': 'Address'}
        address.update({'zipCode': '34732'})
        address.update({'contactName': 'Jane Doe'})
        address.update({'city': 'Istanbul'})
        address.update({'country': 'Turkey'})
        request['shippingAddress'] = address
        request['billingAddress'] = address

        basket_items = []
        basket_item_first = {'id': 'BI101'}
        basket_item_first.update({'name': 'Binocular'})
        basket_item_first.update({'category1': 'Collectibles'})
        basket_item_first.update({'category2': 'Accessories'})
        basket_item_first.update({'itemType': 'PHYSICAL'})
        basket_item_first.update({'price': '0.3'})
        basket_item_first.update({'subMerchantKey': 'sub merchant key'})
        basket_item_first.update({'subMerchantPrice': '0.27'})
        basket_items.append(basket_item_first)

        basket_item_second = {'id': 'BI102'}
        basket_item_second.update({'name': 'Game code'})
        basket_item_second.update({'category1': 'Game'})
        basket_item_second.update({'category2': 'Online Game Items'})
        basket_item_second.update({'itemType': 'VIRTUAL'})
        basket_item_second.update({'price': '0.5'})
        basket_item_second.update({'subMerchantKey': 'sub merchant key'})
        basket_item_second.update({'subMerchantPrice': '0.42'})
        basket_items.append(basket_item_second)

        basket_item_third = {'id': 'BI103'}
        basket_item_third.update({'name': 'Usb'})
        basket_item_third.update({'category1': 'Electronics'})
        basket_item_third.update({'category2': 'Usb / Cable'})
        basket_item_third.update({'itemType': 'PHYSICAL'})
        basket_item_third.update({'price': '0.2'})
        basket_item_third.update({'subMerchantKey': 'sub merchant key'})
        basket_item_third.update({'subMerchantPrice': '0.18'})
        basket_items.append(basket_item_third)

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