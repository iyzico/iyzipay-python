import pprint
import unittest
import iyzipay


class SubMerchantSample(unittest.TestCase):
    def runTest(self):
        self.should_create_personal_sub_merchant()
        self.should_create_private_sub_merchant()
        self.should_create_limited_company_sub_merchant()
        self.should_update_personal_sub_merchant()
        self.should_update_private_sub_merchant()
        self.should_update_limited_company_sub_merchant()
        self.should_retrieve_sub_merchant()

    def should_create_personal_sub_merchant(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['subMerchantExternalId'] = 'B49224'
        request['subMerchantType'] = 'PERSONAL'
        request['address'] = 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1'
        request['contactName'] = 'John'
        request['contactSurname'] = 'Doe'
        request['email'] = 'email@submerchantemail.com'
        request['gsmNumber'] = '+905350000000'
        request['name'] = 'John\'s market'
        request['iban'] = 'TR180006200119000006672315'
        request['identityNumber'] = '1234567890'

        # make request
        sub_merchant = iyzipay.SubMerchant()
        sub_merchant_response = sub_merchant.create(request, options)

        # print response
        pprint.pprint(sub_merchant_response.read().decode())

    def should_create_private_sub_merchant(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['subMerchantExternalId'] = 'S49222'
        request['subMerchantType'] = 'PRIVATE_COMPANY'
        request['address'] = 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1'
        request['taxOffice'] = 'Tax Office'
        request['legalCompanyTitle'] = 'John Doe inc'
        request['email'] = 'email@submerchantemail.com'
        request['gsmNumber'] = '+905350000000'
        request['name'] = 'John\'s market'
        request['iban'] = 'TR180006200119000006672315'
        request['identityNumber'] = '31300864726'

        # make request
        sub_merchant = iyzipay.SubMerchant()
        sub_merchant_response = sub_merchant.create(request, options)

        # print response
        pprint.pprint(sub_merchant_response.read().decode())

    def should_create_limited_company_sub_merchant(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['subMerchantExternalId'] = 'AS49224'
        request['subMerchantType'] = 'LIMITED_OR_JOINT_STOCK_COMPANY'
        request['address'] = 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1'
        request['taxOffice'] = 'Tax Office'
        request['taxNumber'] = '9261877'
        request['legalCompanyTitle'] = 'XYZ inc'
        request['email'] = 'email@submerchantemail.com'
        request['gsmNumber'] = '+905350000000'
        request['name'] = 'John\'s market'
        request['iban'] = 'TR180006200119000006672315'

        # make request
        sub_merchant = iyzipay.SubMerchant()
        sub_merchant_response = sub_merchant.create(request, options)

        # print response
        pprint.pprint(sub_merchant_response.read().decode())

    def should_update_personal_sub_merchant(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['subMerchantKey'] = 'sub merchant key'
        request['iban'] = 'TR180006200119000006672315'
        request['address'] = 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1'
        request['contactName'] = 'Jane'
        request['contactSurname'] = 'Doe'
        request['email'] = 'email@submerchantemail.com'
        request['gsmNumber'] = '+905350000000'
        request['name'] = 'Jane\'s market'
        request['identityNumber'] = '31300864726'

        # make request
        sub_merchant = iyzipay.SubMerchant()
        sub_merchant_response = sub_merchant.update(request, options)

        # print response
        pprint.pprint(sub_merchant_response.read().decode())

    def should_update_private_sub_merchant(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['subMerchantKey'] = 'sub merchant key'
        request['address'] = 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1'
        request['taxOffice'] = 'Tax Office'
        request['legalCompanyTitle'] = 'John Doe inc'
        request['email'] = 'email@submerchantemail.com'
        request['gsmNumber'] = '+905350000000'
        request['name'] = 'John\'s market'
        request['iban'] = 'TR180006200119000006672315'
        request['identityNumber'] = '31300864726'

        # make request
        sub_merchant = iyzipay.SubMerchant()
        sub_merchant_response = sub_merchant.update(request, options)

        # print response
        pprint.pprint(sub_merchant_response.read().decode())

    def should_update_limited_company_sub_merchant(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['subMerchantKey'] = 'sub merchant key'
        request['address'] = 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1'
        request['taxOffice'] = 'Tax Office'
        request['taxNumber'] = '9261877'
        request['legalCompanyTitle'] = 'ABC inc'
        request['email'] = 'email@submerchantemail.com'
        request['gsmNumber'] = '+905350000000'
        request['name'] = 'John\'s market'
        request['iban'] = 'TR180006200119000006672315'

        # make request
        sub_merchant = iyzipay.SubMerchant()
        sub_merchant_response = sub_merchant.update(request, options)

        # print response
        pprint.pprint(sub_merchant_response.read().decode())

    def should_retrieve_sub_merchant(self):
        options = dict([('base_url', iyzipay.base_url)])
        options['api_key'] = iyzipay.api_key
        options['secret_key'] = iyzipay.secret_key

        request = dict([('locale', 'tr')])
        request['conversationId'] = '123456789'
        request['subMerchantExternalId'] = 'AS49224'

        # make request
        sub_merchant = iyzipay.SubMerchant()
        sub_merchant_response = sub_merchant.retrieve(request, options)

        # print response
        pprint.pprint(sub_merchant_response.read().decode())
