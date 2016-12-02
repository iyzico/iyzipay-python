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
    'token': 'token'
}

pecco_payment = iyzipay.PeccoPayment().create(request, options)

print(pecco_payment.read().decode('utf-8'))
