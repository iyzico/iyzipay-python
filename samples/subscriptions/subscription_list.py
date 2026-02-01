import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}


subscription_list = iyzipay.Subscription().retrieve(options)

print(subscription_list.read().decode('utf-8'))
