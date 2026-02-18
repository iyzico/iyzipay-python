import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    "locale": "tr",
    "callbackUrl": "https://www.merchant.com/callback",
    "customerReferenceCode": "7d96e96c-7850-4c63-9ae0-1c9d359e6565"
}

subscription = iyzipay.SubscriptionCardUpdate().initialize(request, options)

print(subscription.read().decode('utf-8'))
