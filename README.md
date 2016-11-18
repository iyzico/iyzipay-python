# iyzipay-python

[![Build Status](https://travis-ci.org/iyzico/iyzipay-python.svg?branch=master)](https://travis-ci.org/iyzico/iyzipay-python)

You can sign up for an iyzico account at https://iyzico.com

# Requirements

Python 2.6 and later.

# Installation

### PyPI

You can install the bindings via [PyPI](https://pypi.python.org). Run the following command:

```bash
pip install iyzipay
```

Or:

```bash
easy_install iyzipay
```

### Manual Installation

If you do not wish to use pip, you can download the [latest release](https://github.com/iyzico/iyzipay-python/releases). Then, to use the bindings, import iyzipay package.

```python
import iyzipay
```

# Usage

```python
options = {
    'api_key': 'your api key',
    'secret_key': 'your secret key',
    'base_url': 'sandbox-api.iyzipay.com'
}

payment_card = {
    'cardHolderName': 'John Doe',
    'cardNumber': '5528790000000008',
    'expireMonth': '12',
    'expireYear': '2030',
    'cvc': '123',
    'registerCard': '0'
}

buyer = {
    'id': 'BY789',
    'name': 'John',
    'surname': 'Doe',
    'gsmNumber': '+905350000000',
    'email': 'email@email.com',
    'identityNumber': '74300864791',
    'lastLoginDate': '2015-10-05 12:43:35',
    'registrationDate': '2013-04-21 15:12:09',
    'registrationAddress': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'ip': '85.34.78.112',
    'city': 'Istanbul',
    'country': 'Turkey',
    'zipCode': '34732'
}

address = {
    'contactName': 'Jane Doe',
    'city': 'Istanbul',
    'country': 'Turkey',
    'address': 'Nidakule Göztepe, Merdivenköy Mah. Bora Sok. No:1',
    'zipCode': '34732'
}

basket_item_first = {
    'id': 'BI101',
    'name': 'Binocular',
    'category1': 'Collectibles',
    'category2': 'Accessories',
    'itemType': 'PHYSICAL',
    'price': '0.3'
}

basket_item_second = {
    'id': 'BI102',
    'name': 'Game code',
    'category1': 'Game',
    'category2': 'Online Game Items',
    'itemType': 'VIRTUAL',
    'price': '0.5'
}

basket_item_third = {
    'id': 'BI103',
    'name': 'Usb',
    'category1': 'Electronics',
    'category2': 'Usb / Cable',
    'itemType': 'PHYSICAL',
    'price': '0.2'
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'price': '1',
    'paidPrice': '1.2',
    'currency': 'TRY',
    'installment': '1',
    'basketId': 'B67832',
    'paymentChannel': 'WEB',
    'paymentGroup': 'PRODUCT',
    'paymentCard': payment_card,
    'buyer': buyer,
    'shippingAddress': address,
    'billingAddress': address,
    'basketItems': [basket_item_first, basket_item_second, basket_item_third]
}

payment = iyzipay.Payment().create(request, options)
```
See other samples under samples directory.