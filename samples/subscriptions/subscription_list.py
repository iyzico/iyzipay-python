import iyzipay

options = {
    'api_key': iyzipay.api_key,
    'secret_key': iyzipay.secret_key,
    'base_url': iyzipay.base_url
}

request = {
    "page": "1",
    "count": "10",
    "subscriptionStatus": "ACTIVE",
    "subscriptionReferenceCode": "c8ab43da-f4b3-40d2-b1ef-620da93ece9",
    "customerReferenceCode": "566b2e1a-5046-4438-9b62-c8cf761f6d1",
    "pricingPlanReferenceCode": "c1d489b6-9adc-42fa-88ae-47ea2e5db1e",
    "parentReferenceCode": "f219267d-ce05-4039-a773-225ea44aad1",
    "startDate": "2026-01-01 08:00:00",
    "endDate": "2025-08-24 20:00:00",
}
subscription_list = iyzipay.Subscription().list(request, options)

print(subscription_list.read().decode('utf-8'))
