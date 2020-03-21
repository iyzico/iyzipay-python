# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': '8138',
    'customerReferenceCode': '2eac778a-1379-4f82-93b1-8bd67ac86c05',
}

report = iyzipay.SubscriptionCustomer().retrieve(request, options)
print(report.read().decode('utf-8'))
