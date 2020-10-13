import iyzipay

options = {
  'api_key': iyzipay.api_key,
  'secret_key': iyzipay.secret_key,
  'base_url': iyzipay.base_url
}

request = {
  "addressIgnorable": False,
  "conversationId": "123456789",
  "currencyCode": "TRY",
  "description": "iyzi product name",
  "encodedImageFile": iyzipay.IyziFileBase64Encoder.encode("image.png"),
  "installmentRequested": False,
  "locale": "tr",
  "name": "iyzi product",
  "price": "22.0",
  "soldLimit": True,
  "token": "ABAraw"
}

report = iyzipay.IyziLinkProduct().update(request, options)
print(report.read().decode('utf-8'))
