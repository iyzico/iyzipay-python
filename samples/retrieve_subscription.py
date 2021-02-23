import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'subscriptionReferenceCode': 'fec5250d-1f9f-4605-bc73-db33072248f7',
}

response = iyzipay.Subscription().retrieve(request, options)

print(response.read().decode('utf-8'))
