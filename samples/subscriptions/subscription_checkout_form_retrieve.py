import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

token = {
    'token': 'b94c27b3-e65f-4e87-880c-54720174d970'
}

checkout_form = iyzipay.SubscriptionCheckoutForm().retrieve(token, options)

print(checkout_form.read().decode('utf-8'))
