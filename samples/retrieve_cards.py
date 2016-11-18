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
    'cardUserKey': 'card user key'
}

card_list = iyzipay.CardList().retrieve(request, options)

print(card_list.read().decode('utf-8'))
