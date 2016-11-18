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

bkm = iyzipay.Bkm().retrieve(request, options)

print(bkm.read().decode('utf-8'))
