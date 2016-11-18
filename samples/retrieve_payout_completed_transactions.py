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

payout_completed_transaction_list = iyzipay.PayoutCompletedTransactionList().retrieve(request, options)

print(payout_completed_transaction_list.read().decode('utf-8'))
