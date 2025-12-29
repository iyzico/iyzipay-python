import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    "locale": "tr",
    "conversationId": "123456789",
    "paymentTransactionId": "20947104",
    "subMerchantKey": "favC6OGPAVHb97HwXG5GPKd4KuE=",
    "subMerchantPrice": "11.0"
}

sub_merchant_item = iyzipay.SubMerchant().update_item(request, options)

print(sub_merchant_item.read().decode('utf-8'))
