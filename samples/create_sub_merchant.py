# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}


def create_personal_sub_merchant():
    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'subMerchantExternalId': 'B49224',
        'subMerchantType': 'PERSONAL',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'contactName': 'John',
        'contactSurname': 'Doe',
        'email': 'email@submerchantemail.com',
        'gsmNumber': '+905350000000',
        'name': 'John\'s market',
        'iban': 'TR180006200119000006672315',
        'identityNumber': '31300864726',
        'currency': 'TRY'
    }

    sub_merchant = iyzipay.SubMerchant().create(request, options)

    print(sub_merchant.read().decode('utf-8'))


def create_private_sub_merchant():
    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'subMerchantExternalId': 'S49222',
        'subMerchantType': 'PRIVATE_COMPANY',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'taxOffice': 'Tax Office',
        'legalCompanyTitle': 'John Doe inc',
        'email': 'email@submerchantemail.com',
        'gsmNumber': '+905350000000',
        'name': 'John\'s market',
        'iban': 'TR180006200119000006672315',
        'identityNumber': '31300864726',
        'currency': 'TRY'
    }

    sub_merchant = iyzipay.SubMerchant().create(request, options)

    print(sub_merchant.read().decode('utf-8'))


def create_limited_company_sub_merchant():
    request = {
        'locale': 'tr',
        'conversationId': '123456789',
        'subMerchantExternalId': 'AS49224',
        'subMerchantType': 'LIMITED_OR_JOINT_STOCK_COMPANY',
        'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
        'taxOffice': 'Tax Office',
        'taxNumber': '9261877',
        'legalCompanyTitle': 'XYZ inc',
        'email': 'email@submerchantemail.com',
        'gsmNumber': '+905350000000',
        'name': 'John\'s market',
        'iban': 'TR180006200119000006672315',
        'currency': 'TRY'
    }

    sub_merchant = iyzipay.SubMerchant().create(request, options)

    print(sub_merchant.read().decode('utf-8'))
