import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

product = {
    'locale': 'tr',
    'conversationId': '123456789',
    'name': 'New Coffee Pack',
    'description': 'Delicious Turkish Coffee',
    'product_reference_code': 'fdb7bc8b-c7a7-44a0-a143-1ce3a6aaeb41'
}

subscription_product = iyzipay.SubscriptionProduct().update(product, options)

print(subscription_product.read().decode('utf-8'))
