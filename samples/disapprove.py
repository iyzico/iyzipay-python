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
    'paymentTransactionId': '1'
}

disapproval = iyzipay.Disapproval().create(request, options)

print(disapproval.read().decode('utf-8'))
