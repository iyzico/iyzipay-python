import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    "callbackUrl": "http://localhost",
    "pricingPlanReferenceCode": "36fcd8e3-f99b-4b19-9dc4-f7c30d7f0cd4",
    "subscriptionInitialStatus": "ACTIVE",
    "conversationId": "123456789",
    "customer": {
        "name": "John",
        "surname": "Stone",
        "email": "john@gmail.com",
        "gsmNumber": "+905545545512",
        "identityNumber": "1234567890",
        "billingAddress": {
            "address": "Altunizade Mah. İnci Çıkmazı Sokak No: 3 İç Kapı No: 10 Üsküdar İstanbul",
            "zipCode": "34345",
            "contactName": "contactName",
            "city": "Istanbul",
            "country": "Türkiye"
        },
        "shippingAddress": {
            "address": "Altunizade Mah. İnci Çıkmazı Sokak No: 3 İç Kapı No: 10 Üsküdar İstanbul",
            "zipCode": "34345",
            "contactName": "contactName",
            "city": "Istanbul",
            "country": "Türkiye"
        }
    }
}

checkout_form = iyzipay.SubscriptionCheckoutForm().create(request, options)

print(checkout_form.read().decode('utf-8'))
