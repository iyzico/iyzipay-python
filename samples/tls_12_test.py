# coding=utf-8

import iyzipay

options = {
    'base_url': 'tlstest.paypal.com'
}

api_test = iyzipay.ApiTest().retrieve(options)

print(api_test.read().decode('utf-8'))
