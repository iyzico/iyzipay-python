import iyzipay

options = {
  'api_key': iyzipay.api_key,
  'secret_key': iyzipay.secret_key,
  'base_url': iyzipay.base_url
}

request = {
  "addressIgnorable": 0,
  "conversationId": "123456789",
  "currencyCode": "TRY",
  "description": "test product new",
  "encodedImageFile": iyzipay.IyziFileBase64Encoder.encode("image.png"),
  "installmentRequested": False,
  "locale": "tr",
  "name": "awsome product",
  "price": "1.0",
  "soldLimit": True
}

report = iyzipay.IyziLinkProduct().create(request, options)
print(report.read().decode('utf-8'))
