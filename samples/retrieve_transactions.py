import iyzipay

options = {
  'api_key': iyzipay.api_key,
  'secret_key': iyzipay.secret_key,
  'base_url': iyzipay.base_url
}

request = {
  'transactionDate': '2019-06-25',
  'page': '1',
}
report = iyzipay.RetrieveTransactions().retrieve(request, options)
print(report.read().decode('utf-8'))
