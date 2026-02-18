import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    "locale": "tr",
    "name": "Orhan",
    "surname": "Test",
    "email": "test@mail.com",
    "gsmNumber": "+905064728758",
    "identityNumber": "111111",
    "billingAddress": {
        "address": "address1",
        "zipCode": "zipCode1",
        "contactName": "contactName1",
        "city": "city1",
        "country": "country1"
    },
    "shippingAddress": {
        "address": "address",
        "zipCode": "zipCode",
        "contactName": "contactName",
        "city": "city",
        "country": "country"
    }
}

subscription = iyzipay.SubscriptionCustomer().create(request, options)

print(subscription.read().decode('utf-8'))
