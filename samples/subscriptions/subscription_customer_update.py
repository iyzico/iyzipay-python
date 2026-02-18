import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    "customerReferenceCode": "994cbfca-2858-42cb-b2f0-5cc81b1f658c",
    "name": "John",
    "surname": "Doe",
    "email": "email@gmail.com",
    "gsmNumber": "+905554443333",
    "identityNumber": "11111111111",
    "billingAddress": {
        "address": "address1",
        "zipCode": "34940",
        "contactName": "John Doe",
        "city": "Istanbul",
        "district": "District",
        "country": "Turkey"
    },
    "shippingAddress": {
        "address": "address",
        "zipCode": "34940",
        "contactName": "John Doe",
        "city": "Istanbul",
        "country": "Turkey"
    }
}

subscription = iyzipay.SubscriptionCustomer().update(request, options)

print(subscription.read().decode('utf-8'))
