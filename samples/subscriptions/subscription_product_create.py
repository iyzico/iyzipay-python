import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

product = {
    'locale': 'tr',
    'conversationId': '123456789',
    'name': 'Coffee Pack',
    'description': 'Turkish Coffee'
}

subscription_product = iyzipay.SubscriptionProduct().create(product, options)

print(subscription_product.read().decode('utf-8'))
