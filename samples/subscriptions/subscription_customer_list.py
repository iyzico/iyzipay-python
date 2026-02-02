import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'page': 1,
    'count': 10,
}

subscription = iyzipay.SubscriptionCustomer().list(request, options)

print(subscription.read().decode('utf-8'))
