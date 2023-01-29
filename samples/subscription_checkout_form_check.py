# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

address = {
    'contactName': 'Jane Doe',
    'city': 'Istanbul',
    'country': 'Turkey',
    'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'zipCode': '34732'
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'pricingPlanReferenceCode': 'b6e6b124-f7bf-452e-b902-1fb3075fae65',
    'name': 'Adı',
    'surname': 'Soyadı',
    'email': 'test@iyzipay.com',
    'gsmNumber': '+905555555555',
    'identityNumber': '00000000000',
    'subscriptionInitialStatus': 'ACTIVE',
    "callbackUrl": "https://www.merchant.com/callback",
    'shippingAddress': address,
    'billingAddress': address,
}

checkout_form_initialize = iyzipay.SubscriptionCheckoutFormInitialize().create(request, options)

print(checkout_form_initialize.read().decode('utf-8'))
