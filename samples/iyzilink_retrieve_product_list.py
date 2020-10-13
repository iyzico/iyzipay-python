import iyzipay

options = {
  'api_key': iyzipay.api_key,
  'secret_key': iyzipay.secret_key,
  'base_url': iyzipay.base_url
}

request = {
  "conversationId": "123456789",
  "locale": "tr",
  "page": 1,
  "count": 1
}

report = iyzipay.IyziLinkProduct().get(request, options)
print(report.read().decode('utf-8'))
