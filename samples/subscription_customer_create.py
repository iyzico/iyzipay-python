# coding=utf-8

import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': '8138',
    'name': 'Müşteri Adı',
    'surname': 'Müşteri Soyadı',
    'email': 'test@bmsumer.com',
    'gsmNumber': '+905445555555',
    'identityNumber': '00000000000',
    'billingAddress': {
        'address': 'Fatura Adres Bilgisi',
        'contactName': 'Fatura Adı Soyadı',
        'city': 'Fatura Şehri',
        'country': 'Fatura Ülkesi',
        'zipCode': 'Fatura Posta Kodu',
    },
    'shippingAddress': {
        'contactName': 'Teslimat Adı Soyadı',
        'city': 'Teslimat Şehri',
        'country': 'Teslimat Ülkesi',
        'address': 'Teslimat Adres Bilgisi',
        'zipCode': 'Teslimat Posta Kodu',
    }

}

report = iyzipay.SubscriptionCustomer().create(request, options)
print(report.read().decode('utf-8'))
