import pprint
import unittest
import iyzipay
import ast
import base64


class ConnectBKMSample(unittest.TestCase):
    def runTest(self):
        self.should_initialize_bkm()
        self.should_retrieve_bkm_auth()

    def should_initialize_bkm(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['price'] = '1'
        request['callbackUrl'] = 'https://www.merchant.com/callback'

        request['buyerId'] = '100'
        request['buyerEmail'] = 'email@email.com'
        request['buyerIp'] = '85.34.78.112'

        request['connectorName'] = 'connector name'

        request['installmentDetails'] = self.prepare_installment_details()

        # make request
        bkm_initialize = iyzipay.ConnectBKMInitialize()
        bkm_initialize_response = bkm_initialize.create(request, options)

        # get and print response
        response = bkm_initialize_response.read().decode()
        pprint.pprint(response)

        # generate html code to redirect to BKM
        response_data_dict = ast.literal_eval(response)
        html_response = base64.b64decode(response_data_dict['htmlContent'])
        pprint.pprint(html_response)

    def should_retrieve_bkm_auth(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['token'] = 'token'

        # make request
        bkm_auth = iyzipay.ConnectBKMAuth()
        bkm_auth_response = bkm_auth.retrieve(request, options)

        # print response
        pprint.pprint(bkm_auth_response.read().decode())

    def prepare_installment_details(self):
        installment_details = list()
        installment_details.append(self.isbank_installment_details())
        installment_details.append(self.finansbank_installment_details())
        installment_details.append(self.akbank_installment_details())
        installment_details.append(self.ykb_installment_details())
        installment_details.append(self.denizbank_installment_details())
        installment_details.append(self.halkbank_installment_details())
        return installment_details

    def isbank_installment_details(self):
        installment_detail = dict([('bankId', '64')])
        installment_prices = []

        single_installment = dict([('installmentNumber', '1',), ('totalPrice', '1')])
        two_installment = dict([('installmentNumber', '2',), ('totalPrice', '1.1')])
        three_installment = dict([('installmentNumber', '3',), ('totalPrice', '1.1')])
        six_installment = dict([('installmentNumber', '6',), ('totalPrice', '1.2')])
        nine_installment = dict([('installmentNumber', '9',), ('totalPrice', '1.4')])

        installment_prices.append(single_installment)
        installment_prices.append(two_installment)
        installment_prices.append(three_installment)
        installment_prices.append(six_installment)
        installment_prices.append(nine_installment)

        installment_detail['installmentPrices'] = installment_prices

        return installment_detail

    def finansbank_installment_details(self):
        installment_detail = dict([('bankId', '111')])
        installment_prices = []

        single_installment = dict([('installmentNumber', '1',), ('totalPrice', '1')])
        two_installment = dict([('installmentNumber', '2',), ('totalPrice', '1.1')])
        three_installment = dict([('installmentNumber', '3',), ('totalPrice', '1.1')])
        six_installment = dict([('installmentNumber', '6',), ('totalPrice', '1.2')])
        nine_installment = dict([('installmentNumber', '9',), ('totalPrice', '1.4')])

        installment_prices.append(single_installment)
        installment_prices.append(two_installment)
        installment_prices.append(three_installment)
        installment_prices.append(six_installment)
        installment_prices.append(nine_installment)

        installment_detail['installmentPrices'] = installment_prices

        return installment_detail

    def akbank_installment_details(self):
        installment_detail = dict([('bankId', '46')])
        installment_prices = []

        single_installment = dict([('installmentNumber', '1',), ('totalPrice', '1')])
        two_installment = dict([('installmentNumber', '2',), ('totalPrice', '1.1')])
        three_installment = dict([('installmentNumber', '3',), ('totalPrice', '1.1')])
        six_installment = dict([('installmentNumber', '6',), ('totalPrice', '1.2')])
        nine_installment = dict([('installmentNumber', '9',), ('totalPrice', '1.4')])

        installment_prices.append(single_installment)
        installment_prices.append(two_installment)
        installment_prices.append(three_installment)
        installment_prices.append(six_installment)
        installment_prices.append(nine_installment)

        installment_detail['installmentPrices'] = installment_prices

        return installment_detail

    def ykb_installment_details(self):
        installment_detail = dict([('bankId', '67')])
        installment_prices = []

        single_installment = dict([('installmentNumber', '1',), ('totalPrice', '1')])
        two_installment = dict([('installmentNumber', '2',), ('totalPrice', '1.1')])
        three_installment = dict([('installmentNumber', '3',), ('totalPrice', '1.1')])
        six_installment = dict([('installmentNumber', '6',), ('totalPrice', '1.2')])
        nine_installment = dict([('installmentNumber', '9',), ('totalPrice', '1.4')])

        installment_prices.append(single_installment)
        installment_prices.append(two_installment)
        installment_prices.append(three_installment)
        installment_prices.append(six_installment)
        installment_prices.append(nine_installment)

        installment_detail['installmentPrices'] = installment_prices

        return installment_detail

    def denizbank_installment_details(self):
        installment_detail = dict([('bankId', '134')])
        installment_prices = []

        single_installment = dict([('installmentNumber', '1',), ('totalPrice', '1')])
        two_installment = dict([('installmentNumber', '2',), ('totalPrice', '1.1')])
        three_installment = dict([('installmentNumber', '3',), ('totalPrice', '1.1')])
        six_installment = dict([('installmentNumber', '6',), ('totalPrice', '1.2')])
        nine_installment = dict([('installmentNumber', '9',), ('totalPrice', '1.4')])

        installment_prices.append(single_installment)
        installment_prices.append(two_installment)
        installment_prices.append(three_installment)
        installment_prices.append(six_installment)
        installment_prices.append(nine_installment)

        installment_detail['installmentPrices'] = installment_prices

        return installment_detail

    def halkbank_installment_details(self):
        installment_detail = dict([('bankId', '12')])
        installment_prices = []

        single_installment = dict([('installmentNumber', '1',), ('totalPrice', '1')])
        two_installment = dict([('installmentNumber', '2',), ('totalPrice', '1.1')])
        three_installment = dict([('installmentNumber', '3',), ('totalPrice', '1.1')])
        six_installment = dict([('installmentNumber', '6',), ('totalPrice', '1.2')])
        nine_installment = dict([('installmentNumber', '9',), ('totalPrice', '1.4')])

        installment_prices.append(single_installment)
        installment_prices.append(two_installment)
        installment_prices.append(three_installment)
        installment_prices.append(six_installment)
        installment_prices.append(nine_installment)

        installment_detail['installmentPrices'] = installment_prices

        return installment_detail


