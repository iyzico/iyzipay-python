import json
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
    'paidPrice': '1.2',
    'ip': '85.34.78.112',
    'currency': 'TRY'
}

payment_postauth = iyzipay.PaymentPostAuth()
payment_postauth_result = payment_postauth.create(request, options)
payment_postauth_result_response = json.load(payment_postauth_result)
print('response:', payment_postauth_result_response)

if payment_postauth_result_response['status'] == 'success':
    secret_key = options['secret_key']
    paymentId = payment_postauth_result_response['paymentId']
    currency = payment_postauth_result_response['currency']
    basketId = payment_postauth_result_response['basketId']
    conversationId = payment_postauth_result_response['conversationId']
    paidPrice = payment_postauth.strip_zero(str(payment_postauth_result_response['paidPrice']))
    price = payment_postauth.strip_zero(str(payment_postauth_result_response['price']))
    signature = payment_postauth_result_response['signature']
    payment_postauth.verify_signature([paymentId, currency, basketId, conversationId, paidPrice, price], secret_key, signature)
