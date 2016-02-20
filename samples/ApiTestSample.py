import pprint

from src.Iyzipay.Model.ApiTest import ApiTest

options = {'api_key': 'apiKey',
           'secret_key': 'secretKey',
           'base_url': 'https://stg.iyzipay.com'}

response = ApiTest.retrieve(options)
pprint.pprint(vars(response))
