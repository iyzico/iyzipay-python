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
    'paymentId': '1',
    'paymentConversationId': '123456789'
}

payment = iyzipay.Payment().retrieve(request, options)

print(payment.read().decode('utf-8'))
