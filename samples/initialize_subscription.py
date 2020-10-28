import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

address = {
    'contactName': 'Jane Doe',
    'city': 'Istanbul',
    'country': 'Turkey',
    'address': 'Uskudar Burhaniye Mahallesi iyzico A.S',
    'zipCode': '34660'
}

customer = {
    'name': 'John',
    'surname': 'Doe',
    'gsmNumber': '+905555555555',
    'email': 'johndoe@iyzico.com',
    'identityNumber': '11111111111',
    'shippingAddress': address,
    'billingAddress': address,
}

payment_card = {
    'cardHolderName': 'John Doe',
    'cardNumber': '4603450000000000',
    'expireMonth': '12',
    'expireYear': '2030',
    'cvc': '123',
    'registerConsumerCard': 'true'
}

request = {
    'locale': 'tr',
    'conversationId': '123456789',
    'pricingPlanReferenceCode': 'c1d489b6-9adc-42fa-88ae-47ea2e5dbe1e',
    'subscriptionInitialStatus': 'ACTIVE',
    'customer': customer,
    'paymentCard': payment_card
}

subscription_initialize = iyzipay.Subscription().create(request, options)

print(subscription_initialize.read().decode('utf-8'))
