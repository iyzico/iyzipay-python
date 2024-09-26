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
    'conversationData': 'conversation data'
}

threeds_payment = iyzipay.ThreedsPayment()
threeds_payment_result = threeds_payment.create(request, options)
threeds_payment_response = json.load(threeds_payment_result)
print('response:', threeds_payment_response)

if threeds_payment_response['status'] == 'success':
    secret_key = options['secret_key']
    paymentId = threeds_payment_response['paymentId']
    currency = threeds_payment_response['currency']
    basketId = threeds_payment_response['basketId']
    conversationId = threeds_payment_response['conversationId']
    paidPrice = str(threeds_payment_response['paidPrice'])
    price = str(threeds_payment_response['price'])
    signature = threeds_payment_response['signature']
    threeds_payment.verify_signature([paymentId, currency, basketId, conversationId, paidPrice, price],secret_key, signature)