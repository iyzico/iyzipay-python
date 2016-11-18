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
    'binNumber': '554960',
    'price': '100'
}

installment_info = iyzipay.InstallmentInfo().retrieve(request, options)

print(installment_info.read().decode('utf-8'))
