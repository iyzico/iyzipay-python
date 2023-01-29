import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

address = {
    'contactName': 'John Doe',
    'city': 'Istanbul',
    'country': 'Turkey',
    'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1'
}

customer = {
    'name': 'John',
    'surname': 'Doe',
    'gsmNumber': '+905350000000',
    'email': 'email@email.com',
    'identityNumber': '11111111111',
    'billingAddress': address
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'callbackUrl': 'https://www.merchant.com/callback',
    'pricingPlanReferenceCode': '123456',
    'subscriptionInitialStatus': 'ACTIVE',
    'customer': customer
}

checkout_form_initialize = iyzipay.SubscriptionCheckoutFormInitialize().create(request, options)

print(checkout_form_initialize.read().decode('utf-8'))
