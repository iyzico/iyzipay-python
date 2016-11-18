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
    'binNumber': '554960'
}

bin_number = iyzipay.BinNumber().retrieve(request, options)

print(bin_number.read().decode('utf-8'))
