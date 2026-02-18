import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'paymentConversationId': '123456s789',
    'paymentId': 1
}
# Both parameters are not mandatory; one of two is enough

report = iyzipay.RetrievePaymentDetails().retrieve(request, options)
print(report.read().decode('utf-8'))
