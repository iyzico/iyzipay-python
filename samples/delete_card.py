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
    'cardToken': 'card token',
    'cardUserKey': 'card user key'
}

card = iyzipay.Card().delete(request, options)

print(card.read().decode('utf-8'))
