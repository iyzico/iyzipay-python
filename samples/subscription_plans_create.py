# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': 1234,
    'name': 'Premium Monthly',
    'price': 500,
    'currencyCode': 'USD',
    'paymentInterval': 'MONTHLY',
    'paymentIntervalCount': 1,
    'trialPeriodDays': 30,
    'planPaymentType': 'RECURRING',
    'recurrenceCount': 12,
    'referenceCode': '6b4803fb-c4f0-4f37-9df7-899a186e1451'
}

report = iyzipay.SubscriptionPlan().create(request, options)
print(report.read().decode('utf-8'))
