import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'paymentId': '1',
    'ip': '85.34.78.112',
    'reason': 'other',
    'description': 'customer requested for default sample'
}

cancel = iyzipay.Cancel().create(request, options)

print(cancel.read().decode('utf-8'))
