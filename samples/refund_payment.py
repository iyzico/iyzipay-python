import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    "locale": "tr",
    "conversationId": "conversationId",
    "paymentId": "2921546163",
    "price": "3.0",
    "ip": "85.34.78.112"
}

sub_merchant = iyzipay.Payment().refund(request, options)

print(sub_merchant.read().decode('utf-8'))
