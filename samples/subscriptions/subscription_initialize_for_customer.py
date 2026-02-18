import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'subscriptionInitialStatus': 'ACTIVE',
    'pricingPlanReferenceCode': '36fcd8e3-f99b-4b19-9dc4-f7c30d7f0cd4',
    'customerReferenceCode': 'c9fba719-bf17-45fa-9cc7-8fbb70321023'
}

subscription = iyzipay.Subscription().initialize_with_customer(request, options)

print(subscription.read().decode('utf-8'))
