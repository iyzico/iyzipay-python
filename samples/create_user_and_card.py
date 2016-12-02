# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

card_information = {
    'cardAlias': 'card alias',
    'cardHolderName': 'John Doe',
    'cardNumber': '5528790000000008',
    'expireMonth': '12',
    'expireYear': '2030'
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'email': 'email@email.com',
    'externalId': 'external id',
    'card': card_information
}

card = iyzipay.Card().create(request, options)

print(card.read().decode('utf-8'))
