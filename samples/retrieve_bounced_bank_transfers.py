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
    'date': '2016-01-22 19:13:00'
}

bounced_bank_transfer_list = iyzipay.BouncedBankTransferList().retrieve(request, options)

print(bounced_bank_transfer_list.read().decode('utf-8'))
