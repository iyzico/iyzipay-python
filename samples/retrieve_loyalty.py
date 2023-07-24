import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

payment_card = {
    'cardHolderName': 'John Doe',
    'cardNumber': '5482370000000003',
    'expireMonth': '12',
    'expireYear': '2030',
    'cvc': '123'
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'currency': 'TRY',
    'paymentCard': payment_card
}

loyalty = iyzipay.RetrieveLoyalty().retrieve(request, options)

print(loyalty.read().decode('utf-8'))
