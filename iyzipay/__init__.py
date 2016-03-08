# Iyzipay API python client
# API docs at https://iyzico.com
# Authors:
# Yalcin Yenigun <yalcin.yenigun@iyzico.com>
# Nurettin Bakkal <nurettin.bakkal@iyzico.com>

# Configuration variables
api_key = 'api key'
secret_key = 'secret key'
base_url = 'stg.iyzipay.com'

# Resource
from iyzipay.iyzipay_resource import (  # noqa
    ApiTest,
    BinNumber)
