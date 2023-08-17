import iyzipay

options = {
    'base_url': iyzipay.base_url
}

api_test = iyzipay.ApiTest().retrieve(options)

print(api_test.body)
