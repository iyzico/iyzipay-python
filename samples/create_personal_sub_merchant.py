import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'subMerchantExternalId': 'B49224',
    'subMerchantType': 'PERSONAL',
    'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'contactName': 'John',
    'contactSurname': 'Doe',
    'email': 'email@submerchantemail.com',
    'gsmNumber': '+905350000000',
    'name': 'John\'s market',
    'iban': 'TR180006200119000006672315',
    'identityNumber': '31300864726',
    'currency': 'TRY'
}

sub_merchant = iyzipay.SubMerchant().create(request, options)

print(sub_merchant.read().decode('utf-8'))
