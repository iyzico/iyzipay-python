import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    "locale": "tr",
    "pricingPlanReferenceCode": "36fcd8e3-f99b-4b19-9dc4-f7c30d7f0cd4",
    "conversationId": "conv-1001",
    "subscriptionInitialStatus": "ACTIVE",
    "customer": {
        "name": "John",
        "surname": "Stone",
        "email": "john@gmail.com",
        "gsmNumber": "+905545545512",
        "identityNumber": "1234567890",
        "billingAddress": {
            "address": "Altunizade Mah. İnci Çıkmazı Sokak No: 3 İç Kapı No: 10 Üsküdar İstanbul",
            "contactName": "contactName",
            "city": "Istanbul",
            "country": "Türkiye"
        },
        "shippingAddress": {
            "address": "address",
            "zipCode": "zipCode",
            "contactName": "contactName",
            "city": "city",
            "country": "country"
        }
    },
    "paymentCard": {
        "cardHolderName": "John Doe",
        "cardNumber": "5528790000000008",
        "expireMonth": "12",
        "expireYear": "2030",
        "cvc": "123"
    }
}

subscription = iyzipay.Subscription().initialize(request, options)

print(subscription.read().decode('utf-8'))
