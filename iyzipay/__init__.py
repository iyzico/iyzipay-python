# Iyzipay API python client
# API docs at https://iyzico.com
# Authors:
# Yalcin Yenigun <yalcin.yenigun@iyzico.com>
# Nurettin Bakkal <nurettin.bakkal@iyzico.com>

# Configuration variables
api_key = 'mrI3mIMuNwGiIxanQslyJBRYa8nYrCU5'
secret_key = '9lkVluNHBABPw0LIvyn50oYZcrSJ8oNo'
base_url = 'localhost:8080'

# Resource
from iyzipay.iyzipay_resource import (  # noqa
    ApiTest,
    BinNumber,
    Approval,
    BKMAuth,
    BKMInitialize)

from iyzipay.pki_builder import (  # noqa
    PKIBuilder
)
