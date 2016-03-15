import pprint
import unittest
import iyzipay
import ast
import base64


class CheckoutFormSample(unittest.TestCase):
    def runTest(self):
        self.should_initialize_checkout_form()
        self.should_retrieve_checkout_form_auth()

    def should_initialize_checkout_form(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['price'] = '1'
        request['paidPrice'] = '1.2'
        request['basketId'] = 'B67832'
        request['paymentGroup'] = 'PRODUCT'
        request['callbackUrl'] = 'https://www.merchant.com/callback'

        buyer = dict([('id', 'BY789')])
        buyer['name'] = 'John'
        buyer['surname'] = 'Doe'
        buyer['gsmNumber'] = '+905350000000'
        buyer['email'] = 'email@email.com'
        buyer['identityNumber'] = '74300864791'
        buyer['lastLoginDate'] = '2015-10-05 12:43:35'
        buyer['registrationDate'] = '2013-04-21 15:12:09'
        buyer['registrationAddress'] = 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1'
        buyer['ip'] = '85.34.78.112'
        buyer['city'] = 'Istanbul'
        buyer['country'] = 'Turkey'
        buyer['zipCode'] = '34732'
        request['buyer'] = buyer

        address = dict([('address', 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1')])
        address['zipCode'] = '34732'
        address['contactName'] = 'Jane Doe'
        address['city'] = 'Istanbul'
        address['country'] = 'Turkey'
        request['shippingAddress'] = address
        request['billingAddress'] = address

        basket_items = []
        basket_item_first = dict([('id', 'BI101')])
        basket_item_first['name'] = 'Binocular'
        basket_item_first['category1'] = 'Collectibles'
        basket_item_first['category2'] = 'Accessories'
        basket_item_first['itemType'] = 'PHYSICAL'
        basket_item_first['price'] = '0.3'
        basket_item_first['subMerchantKey'] = 'sub merchant key'
        basket_item_first['subMerchantPrice'] = '0.27'
        basket_items.append(basket_item_first)

        basket_item_second = dict([('id', 'BI102')])
        basket_item_second['name'] = 'Game code'
        basket_item_second['category1'] = 'Game'
        basket_item_second['category2'] = 'Online Game Items'
        basket_item_second['itemType'] = 'VIRTUAL'
        basket_item_second['price'] = '0.5'
        basket_item_second['subMerchantKey'] = 'sub merchant key'
        basket_item_second['subMerchantPrice'] = '0.42'
        basket_items.append(basket_item_second)

        basket_item_third = dict([('id', 'BI103')])
        basket_item_third['name'] = 'Usb'
        basket_item_third['category1'] = 'Electronics'
        basket_item_third['category2'] = 'Usb / Cable'
        basket_item_third['itemType'] = 'PHYSICAL'
        basket_item_third['price'] = '0.2'
        basket_item_third['subMerchantKey'] = 'sub merchant key'
        basket_item_third['subMerchantPrice'] = '0.18'
        basket_items.append(basket_item_third)

        request['basketItems'] = basket_items

        # make request
        checkout_form_initialize = iyzipay.CheckoutFormInitialize()
        checkout_form_initialize_response = checkout_form_initialize.create(request, options)

        # get and print response
        response = checkout_form_initialize_response.read().decode()
        pprint.pprint(response)

    def should_retrieve_checkout_form_auth(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['token'] = 'token'

        # make request
        checkout_form_auth = iyzipay.CheckoutFormAuth()
        checkout_form_auth_response = checkout_form_auth.retrieve(request, options)

        # print response
        pprint.pprint(checkout_form_auth_response.read().decode())
