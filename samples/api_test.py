import iyzipay

options = {
    'secret_key': iyzipay.secret_key,
    'api_key': iyzipay.api_key,
    'base_url': iyzipay.base_url,
}

api_test = iyzipay.ApiTest().retrieve(options)

print(api_test.read().decode('utf-8'))
