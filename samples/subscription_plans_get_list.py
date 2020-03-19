# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'referenceCode': '6b4803fb-c4f0-4f37-9df7-899a186e1451'
}

report = iyzipay.SubscriptionPlan().get(request, options)
print(report.read().decode('utf-8'))
