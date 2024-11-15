import json
import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

payment_card = {
    'cardHolderName': 'John Doe',
    'cardNumber': '5528790000000008',
    'expireMonth': '12',
    'expireYear': '2030',
    'cvc': '123',
    'registerCard': '0'
}

buyer = {
    'id': 'BY789',
    'name': 'John',
    'surname': 'Doe',
    'gsmNumber': '+905350000000',
    'email': 'email@email.com',
    'identityNumber': '74300864791',
    'lastLoginDate': '2015-10-05 12:43:35',
    'registrationDate': '2013-04-21 15:12:09',
    'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'ip': '85.34.78.112',
    'city': 'Istanbul',
    'country': 'Turkey',
    'zipCode': '34732'
}

address = {
    'contactName': 'Jane Doe',
    'city': 'Istanbul',
    'country': 'Turkey',
    'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'zipCode': '34732'
}

basket_items = [
    {
        'id': 'BI101',
        'name': 'Binocular',
        'category1': 'Collectibles',
        'category2': 'Accessories',
        'itemType': 'PHYSICAL',
        'price': '0.3'
    },
    {
        'id': 'BI102',
        'name': 'Game code',
        'category1': 'Game',
        'category2': 'Online Game Items',
        'itemType': 'VIRTUAL',
        'price': '0.5'
    },
    {
        'id': 'BI103',
        'name': 'Usb',
        'category1': 'Electronics',
        'category2': 'Usb / Cable',
        'itemType': 'PHYSICAL',
        'price': '0.2'
    }
]

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'price': '1',
    'paidPrice': '1.2',
    'currency': 'TRY',
    'installment': '1',
    'basketId': 'B67832',
    'paymentChannel': 'WEB',
    'paymentGroup': 'PRODUCT',
    'paymentCard': payment_card,
    'buyer': buyer,
    'shippingAddress': address,
    'billingAddress': address,
    'basketItems': basket_items
}

payment_preauth = iyzipay.PaymentPreAuth()
payment_preauth_result = payment_preauth.create(request, options)
payment_preauth_result_response = json.load(payment_preauth_result)
print('response:', payment_preauth_result_response)

if payment_preauth_result_response['status'] == 'success':
    secret_key = options['secret_key']
    paymentId = payment_preauth_result_response['paymentId']
    currency = payment_preauth_result_response['currency']
    basketId = payment_preauth_result_response['basketId']
    conversationId = payment_preauth_result_response['conversationId']
    paidPrice = payment_preauth.strip_zero(str(payment_preauth_result_response['paidPrice']))
    price = payment_preauth.strip_zero(str(payment_preauth_result_response['price']))
    signature = payment_preauth_result_response['signature']
    payment_preauth.verify_signature([paymentId, currency, basketId, conversationId, paidPrice, price],secret_key, signature)