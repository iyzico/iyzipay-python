# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'referenceCode': 'b6e6b124-f7bf-452e-b902-1fb3075fae65'
}

report = iyzipay.SubscriptionPlan().delete(request, options)
print(report.read().decode('utf-8'))
