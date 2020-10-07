import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'paymentTransactionId': '1',
    'price': '0.5',
    'currency': 'TRY',
    'ip': '85.34.78.112',
    'reason': 'other',
    'description': 'customer requested for default sample'
}

refund = iyzipay.Refund().create(request, options)

print(refund.read().decode('utf-8'))
