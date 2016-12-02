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

checkout_form_result = iyzipay.CheckoutForm().retrieve(request, options)

print(checkout_form_result.read().decode('utf-8'))
