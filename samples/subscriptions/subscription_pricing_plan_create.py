import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

pricing_plan = {
    'locale': 'tr',
    'conversationId': 'conv-001',
    'name': 'Aylık Plan',
    'recurrenceCount': 12,
    'planPaymentType': 'RECURRING',
    'trialPeriodDays': 0,
    'paymentIntervalCount': 1,
    'paymentInterval': 'MONTHLY',
    'currencyCode': 'TRY',
    'price': 99.99,
    'product_reference_code': 'fe7b7a27-4192-45da-964e-7a5934b3a6ef'
}

subscription_product = iyzipay.SubscriptionPricingPlan().create(pricing_plan, options)

print(subscription_product.read().decode('utf-8'))
