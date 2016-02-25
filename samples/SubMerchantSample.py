import pprint
import unittest

from samples.BaseSample import BaseSample
from src.Iyzipay.Model.SubMerchant import SubMerchant


class SubMerchantSample(BaseSample, unittest.TestCase):
    def runTest(self):
        self.should_create_personal_sub_merchant()
        self.should_create_private_sub_merchant()
        self.should_create_limited_company_sub_merchant()
        self.should_update_personal_sub_merchant()
        self.should_update_private_sub_merchant()
        self.should_update_limited_company_sub_merchant()
        self.should_retrieve_sub_merchant()

    def should_create_personal_sub_merchant(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'sub_merchant_external_id': 'B49224',
                   'sub_merchant_type': 'PERSONAL',
                   'address': 'Address',
                   'contact_name': 'John',
                   'contact_surname': 'Doe',
                   'email': 'email@submerchantemail.com',
                   'gsm_number': '+905350000000',
                   'name': 'John\'s market',
                   'iban': 'TR180006200119000006672315',
                   'identity_number': '1234567890'}

        sub_merchant = SubMerchant.create(request, BaseSample.options)

        pprint.pprint(sub_merchant)

    def should_create_private_sub_merchant(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'sub_merchant_external_id': 'B49224',
                   'sub_merchant_type': 'PRIVATE_COMPANY',
                   'address': 'Address',
                   'tax_office': 'Tax office',
                   'legal_company_title': 'John Doe Inc',
                   'email': 'email@submerchantemail.com',
                   'gsm_number': '+905350000000',
                   'name': 'John\'s market',
                   'iban': 'TR180006200119000006672315',
                   'identity_number': '1234567890'}

        sub_merchant = SubMerchant.create(request, BaseSample.options)

        pprint.pprint(sub_merchant)

    def should_create_limited_company_sub_merchant(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'sub_merchant_external_id': 'B49224',
                   'sub_merchant_type': 'LIMITED_OR_JOINT_STOCK_COMPANY',
                   'address': 'Address',
                   'tax_office': 'Tax office',
                   'tax_number': '9261877',
                   'legal_company_title': 'XYZ inc',
                   'email': 'email@submerchantemail.com',
                   'gsm_number': '+905350000000',
                   'name': 'John\'s market',
                   'iban': 'TR180006200119000006672315'}

        sub_merchant = SubMerchant.create(request, BaseSample.options)

        pprint.pprint(sub_merchant)

    def should_update_personal_sub_merchant(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'sub_merchant_key': 'sub merchant key',
                   'iban': 'TR180006200119000006672315',
                   'address': 'Address',
                   'contact_name': 'Jane',
                   'contact_surname': 'Doe',
                   'email': 'email@submerchantemail.com',
                   'gsm_number': '+905350000000',
                   'name': 'John\'s market',
                   'identity_number': '31300864726'}

        subMerchant = SubMerchant.update(request, BaseSample.options)

        pprint.pprint(subMerchant)

    def should_update_private_sub_merchant(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'sub_merchant_key': 'sub merchant key',
                   'address': 'Address',
                   'tax_office': 'Tax office',
                   'legal_company_title': 'Jane Doe Inc',
                   'email': 'email@submerchantemail.com',
                   'gsm_number': '+905350000000',
                   'name': 'Jane\'s market',
                   'iban': 'TR180006200119000006672315',
                   'identity_number': '31300864726'}

        subMerchant = SubMerchant.update(request, BaseSample.options)

        pprint.pprint(subMerchant)

    def should_update_limited_company_sub_merchant(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'sub_merchant_key': 'sub merchant key',
                   'address': 'Address',
                   'tax_office': 'Tax office',
                   'tax_number': '9261877',
                   'legal_company_title': 'Jane Doe Inc',
                   'email': 'email@submerchantemail.com',
                   'gsm_number': '+905350000000',
                   'name': 'Jane\'s market',
                   'iban': 'TR180006200119000006672315'}

        subMerchant = SubMerchant.update(request, BaseSample.options)

        pprint.pprint(subMerchant)

    def should_retrieve_sub_merchant(self):
        request = {'locale': 'tr',
                   'conversation_id': '123456789',
                   'sub_merchant_external_id': 'AS49224'}

        sub_merchant = SubMerchant.retrieve(request, BaseSample.options)

        pprint.pprint(sub_merchant)

