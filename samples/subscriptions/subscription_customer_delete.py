import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'customerReferenceCode': '994cbfca-2858-42cb-b2f0-5cc81b1f658c'
}

subscription = iyzipay.SubscriptionCustomer().delete(request, options)

print(subscription.read().decode('utf-8'))
