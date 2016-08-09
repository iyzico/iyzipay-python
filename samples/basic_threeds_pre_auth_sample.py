# coding=utf-8
import unittest
import iyzipay
import ast
import base64


class BasicThreedsPreAuthSample(unittest.TestCase):
    def runTest(self):
        self.should_initialize_threeds_with_card()
        self.should_initialize_threeds_with_card_token()
        self.should_auth_threeds()

    def should_initialize_threeds_with_card(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['price'] = '1'
        request['paidPrice'] = '1'
        request['installment'] = '1'
        request['buyerEmail'] = 'email@email.com'
        request['buyerId'] = 'B2323'
        request['buyerIp'] = '85.34.78.112'
        request['connectorName'] = 'connector name'
        request['callbackUrl'] = 'https://www.merchant.com/callback'
        request['currency'] = 'TRY'
        request['connectorName'] = 'connector name'

        payment_card = dict([('cardHolderName', 'John Doe')])
        payment_card['cardNumber'] = '5528790000000008'
        payment_card['expireMonth'] = '12'
        payment_card['expireYear'] = '2030'
        payment_card['cvc'] = '123'
        payment_card['registerCard'] = '0'
        request['paymentCard'] = payment_card

        # make request
        basic_threeds_initialize_pre_auth = iyzipay.BasicThreedsInitializePreAuth()
        basic_threeds_initialize_pre_auth_response = basic_threeds_initialize_pre_auth.create(request, options)

        # get and print response
        response = basic_threeds_initialize_pre_auth_response.read().decode('utf-8')
        print(response)

        # generate html code to redirect to BKM
        response_data_dict = ast.literal_eval(response)
        html_response = base64.b64decode(response_data_dict['threeDSHtmlContent']).decode('utf-8')
        print(html_response)

    def should_initialize_threeds_with_card_token(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['price'] = '1'
        request['paidPrice'] = '1'
        request['installment'] = '1'
        request['buyerEmail'] = 'email@email.com'
        request['buyerId'] = 'B2323'
        request['buyerIp'] = '85.34.78.112'
        request['connectorName'] = 'connector name'
        request['currency'] = 'TRY'
        request['callbackUrl'] = 'https://www.merchant.com/callback'
        request['connectorName'] = 'connector name'

        payment_card = dict([('cardToken', 'card token')])
        payment_card['cardUserKey'] = 'card user key'
        request['paymentCard'] = payment_card

        # make request
        basic_threeds_initialize_pre_auth = iyzipay.BasicThreedsInitializePreAuth()
        basic_threeds_initialize_pre_auth_response = basic_threeds_initialize_pre_auth.create(request, options)

        # get and print response
        response = basic_threeds_initialize_pre_auth_response.read().decode('utf-8')
        print(response)

        # generate html code to redirect to BKM
        response_data_dict = ast.literal_eval(response)
        html_response = base64.b64decode(response_data_dict['threeDSHtmlContent']).decode('utf-8')
        print(html_response)

    def should_auth_threeds(self):

        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['paymentId'] = '1'
        request['conversationData'] = 'conversation data'

        # make request
        basic_threeds_payment = iyzipay.BasicThreedsPayment()
        basic_threeds_payment_response = basic_threeds_payment.create(request, options)

        # print response
        print(basic_threeds_payment_response.read().decode('utf-8'))


