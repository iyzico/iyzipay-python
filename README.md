# iyzipay-python

You can sign up for an iyzico account at https://iyzico.com

# Requirements

Python 3.6+

### Deprecation Notes

- Python 2.7 will not be maintained past 2020. As we iyzico, we will not support of that python version at March of 2020. If you have any questions, please open an issue on Github or contact us at integration@iyzico.com.
- Python 3.2, 3.3, 3.4 and 3.5 supports are dropped after v1.0.37.

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

basket_items = [
    {
        'id': 'BI101',
        'name': 'Binocular',
        'category1': 'Collectibles',
        'category2': 'Accessories',
        'itemType': 'PHYSICAL',
        'price': '0.3'
    },
    {
        'id': 'BI102',
        'name': 'Game code',
        'category1': 'Game',
        'category2': 'Online Game Items',
        'itemType': 'VIRTUAL',
        'price': '0.5'
    },
    {
        'id': 'BI103',
        'name': 'Usb',
        'category1': 'Electronics',
        'category2': 'Usb / Cable',
        'itemType': 'PHYSICAL',
        'price': '0.2'
    }
]

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
    'basketItems': basket_items
}

payment = iyzipay.Payment().create(request, options)
```
See other samples under samples directory.

### Mock test cards

Test cards that can be used to simulate a *successful* payment:

Card Number      | Bank                       | Card Type
-----------      | ----                       | ---------
5890040000000016 | Akbank                     | Master Card (Debit)  
5526080000000006 | Akbank                     | Master Card (Credit)  
4766620000000001 | Denizbank                  | Visa (Debit)  
4603450000000000 | Denizbank                  | Visa (Credit)
4729150000000005 | Denizbank Bonus            | Visa (Credit)  
4987490000000002 | Finansbank                 | Visa (Debit)  
5311570000000005 | Finansbank                 | Master Card (Credit)  
9792020000000001 | Finansbank                 | Troy (Debit)  
9792030000000000 | Finansbank                 | Troy (Credit)  
5170410000000004 | Garanti Bankası            | Master Card (Debit)  
5400360000000003 | Garanti Bankası            | Master Card (Credit)  
374427000000003  | Garanti Bankası            | American Express  
4475050000000003 | Halkbank                   | Visa (Debit)  
5528790000000008 | Halkbank                   | Master Card (Credit)  
4059030000000009 | HSBC Bank                  | Visa (Debit)  
5504720000000003 | HSBC Bank                  | Master Card (Credit)  
5892830000000000 | Türkiye İş Bankası         | Master Card (Debit)  
4543590000000006 | Türkiye İş Bankası         | Visa (Credit)  
4910050000000006 | Vakıfbank                  | Visa (Debit)  
4157920000000002 | Vakıfbank                  | Visa (Credit)  
5168880000000002 | Yapı ve Kredi Bankası      | Master Card (Debit)  
5451030000000000 | Yapı ve Kredi Bankası      | Master Card (Credit)  

*Cross border* test cards:

Card Number      | Country
-----------      | -------
4054180000000007 | Non-Turkish (Debit)
5400010000000004 | Non-Turkish (Credit)  

Test cards to get specific *error* codes:

Card Number       | Description
-----------       | -----------
5406670000000009  | Success but cannot be cancelled, refund or post auth
4111111111111129  | Not sufficient funds
4129111111111111  | Do not honour
4128111111111112  | Invalid transaction
4127111111111113  | Lost card
4126111111111114  | Stolen card
4125111111111115  | Expired card
4124111111111116  | Invalid cvc2
4123111111111117  | Not permitted to card holder
4122111111111118  | Not permitted to terminal
4121111111111119  | Fraud suspect
4120111111111110  | Pickup card
4130111111111118  | General error
4131111111111117  | Success but mdStatus is 0
4141111111111115  | Success but mdStatus is 4
4151111111111112  | 3dsecure initialize failed
