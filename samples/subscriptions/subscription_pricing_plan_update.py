import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    'name': 'Aylık Yeni Plan',
    'trialPeriodDays': 5,
    'pricing_plan_reference_code': 'e0b8e566-5c6c-430f-8b6e-281c44215bbf'
}

subscription_pricing_plan = iyzipay.SubscriptionPricingPlan().update(request, options)

print(subscription_pricing_plan.read().decode('utf-8'))
