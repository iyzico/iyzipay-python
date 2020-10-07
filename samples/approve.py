import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'paymentTransactionId': '1'
}

approval = iyzipay.Approval().create(request, options)

print(approval.read().decode('utf-8'))
