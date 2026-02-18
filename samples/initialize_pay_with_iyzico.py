import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

buyer = {
    "id": "buyerID",
    "name": "buyerName",
    "surname": "buyerSurname",
    "identityNumber": "11111",
    "email": "test@gmail.com",
    "gsmNumber": "+905554443322",
    "registrationAddress": "Burhaniye Mahallesi Atilla Sokak No:7 Üsküdar",
    "city": "Istanbul",
    "country": "Turkey",
    "ip": "85.34.78.112"
}

address = {
    "address": "Burhaniye Mahallesi Atilla Sokak No:7 Üsküdar",
    "contactName": "Contact Name",
    "city": "Istanbul",
    "country": "Turkey"
}

basket_items = [
    {
        "id": "ItemID",
        "price": "1000.0",
        "name": "IPHONE 11 64GB WHITE NON ACC Beden:KK06 ,Renk:Beyaz",
        "category1": "IPHONE 11",
        "itemType": "PHYSICAL",
        "chargedFromMerchant": "True"
    }
]

request = {
    "locale": "tr",
    "conversationId": "conversationID",
    "price": "1000.0",
    "basketId": "B67832",
    "paymentGroup": "PRODUCT",
    "callbackUrl": "https://callback.requestcatcher.com/test",
    "currency": "TRY",
    "cancelUrl": "https://www.cancelUrl.com/",
    "paidPrice": "30.0",
    "enabledInstallments": [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    ],
    'buyer': buyer,
    'shippingAddress': address,
    'billingAddress': address,
    'basketItems': basket_items
}

report = iyzipay.PayWithIyzico().create(request, options)

print(report.read().decode('utf-8'))
