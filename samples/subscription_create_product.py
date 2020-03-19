# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': 1234,
    'name': 'Standart',
    'Description': 'Standart Test Product Description'
}

report = iyzipay.SubscriptionProduct().create(request, options)
print(report.read().decode('utf-8'))
