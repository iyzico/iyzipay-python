import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'product_reference_code': '9f7cbae3-bb85-4649-981c-707ac034ca4d'
}

subscription_product = iyzipay.SubscriptionProduct().retrieve(request, options)

print(subscription_product.read().decode('utf-8'))
