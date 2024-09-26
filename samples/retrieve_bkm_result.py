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
    'token': 'mockToken_1727280290715'
}

bkm = iyzipay.Bkm()
bkm_retrieve_result = bkm.retrieve(request, options)
bkm_retrieve_response = json.load(bkm_retrieve_result)
print('response:', bkm_retrieve_response)

if bkm_retrieve_response['status'] == 'success':
    secret_key = options['secret_key']
    paymentId = bkm_retrieve_response['paymentId']
    paymentStatus = bkm_retrieve_response['paymentStatus']
    basketId = bkm_retrieve_response['basketId']
    conversationId = bkm_retrieve_response['conversationId']
    currency = bkm_retrieve_response['currency']
    paidPrice = str(bkm_retrieve_response['paidPrice'])
    price = str(bkm_retrieve_response['price'])
    token = bkm_retrieve_response['token']
    signature = bkm_retrieve_response['signature']
    bkm.verify_signature([paymentId, paymentStatus, basketId, conversationId, currency, paidPrice, price, token], secret_key, signature)