import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    "subscriptionReferenceCode": "a2077643-bab7-4b73-85a5-7676c78d7c66",
    "newPricingPlanReferenceCode": "dbffa857-40f5-48d1-9179-e9326ffb942d",
    "upgradePeriod": "NEXT_PERIOD",
    "useTrial": False,
    "resetRecurrenceCount": True
}

subscription = iyzipay.Subscription().upgrade(request, options)

print(subscription.read().decode('utf-8'))
