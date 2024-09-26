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
    'paymentConversationId': '123456789'
}

payment_retrieve = iyzipay.Payment()
payment_retrieve_result = payment_retrieve.retrieve(request, options)
payment_retrieve_response = json.load(payment_retrieve_result)
print('response:', payment_retrieve_response)

if payment_retrieve_response['status'] == 'success':
    secret_key = options['secret_key']
    paymentId = payment_retrieve_response['paymentId']
    currency = payment_retrieve_response['currency']
    basketId = payment_retrieve_response['basketId']
    conversationId = payment_retrieve_response['conversationId']
    paidPrice = payment_retrieve.strip_zero(str(payment_retrieve_response['paidPrice']))
    price = payment_retrieve.strip_zero(str(payment_retrieve_response['price']))
    signature = payment_retrieve_response['signature']
    payment_retrieve.verify_signature([paymentId, currency, basketId, conversationId, paidPrice, price], secret_key, signature)