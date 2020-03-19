# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'name': 'Standart Update',
    'referenceCode': "8df0a549-ab22-43ce-a31d-0c38be9723b0",
}

report = iyzipay.SubscriptionProduct().update(request, options)
print(report.read().decode('utf-8'))
