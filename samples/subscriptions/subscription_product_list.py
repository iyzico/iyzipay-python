import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

subscription_product = iyzipay.SubscriptionProduct().list(options)

print(subscription_product.read().decode('utf-8'))
