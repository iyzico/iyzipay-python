import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'page': 1,
    'count': 10,
    'product_reference_code': 'fe7b7a27-4192-45da-964e-7a5934b3a6ef'
}

subscription_product = iyzipay.SubscriptionPricingPlan().list(request, options)

print(subscription_product.read().decode('utf-8'))
