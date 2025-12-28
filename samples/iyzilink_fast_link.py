import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    "description": "ft-description-fast-link",
    "price": 10,
    "currencyCode": "TRY",
    "sourceType": "WEB",
    "locale": "tr",
    "conversationId": "123456789"
}

report = iyzipay.IyziLinkProduct().fast_link(request, options)
print(report.read().decode('utf-8'))
