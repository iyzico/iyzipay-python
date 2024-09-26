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
    'token': 'token'
}

checkout_form_retrieve = iyzipay.CheckoutForm()
checkout_form_retrieve_result = checkout_form_retrieve.retrieve(request, options)
checkout_form_retrieve_response = json.load(checkout_form_retrieve_result)
print('response:', checkout_form_retrieve_response)

if checkout_form_retrieve_response['status'] == 'success':
    secret_key = options['secret_key']
    paymentStatus = checkout_form_retrieve_response['paymentStatus']
    paymentId = checkout_form_retrieve_response['paymentId']
    currency = checkout_form_retrieve_response['currency']
    basketId = checkout_form_retrieve_response['basketId']
    conversationId = checkout_form_retrieve_response['conversationId']
    paidPrice = str(checkout_form_retrieve_response['paidPrice'])
    price = str(checkout_form_retrieve_response['price'])
    token = checkout_form_retrieve_response['token']
    signature = checkout_form_retrieve_response['signature']
    checkout_form_retrieve.verify_signature([paymentStatus, paymentId, currency, basketId, conversationId, paidPrice, price, token], secret_key, signature)
