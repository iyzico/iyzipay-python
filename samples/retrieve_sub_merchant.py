# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'subMerchantExternalId': 'AS49224'
}

sub_merchant = iyzipay.SubMerchant().retrieve(request, options)

print(sub_merchant.read().decode('utf-8'))
