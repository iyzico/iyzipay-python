from src.Iyzipay.HttpClient import HttpClient
from src.Iyzipay.IyzipayResource import IyzipayResource
from src.Iyzipay.JsonBuilder import JsonBuilder
from src.Iyzipay.RequestStringBuilder import RequestStringBuilder


class SubMerchant(IyzipayResource):
    @classmethod
    def create(cls, request, options):
        json_encoded_request = cls.get_json_object(request)
        pki_string_request = cls.to_pki_request_string(request)
        raw_result = HttpClient.create().post(options['base_url'] + "/onboarding/submerchant",
                                              IyzipayResource.get_http_header(pki_string_request, options),
                                              json_encoded_request)
        json_result = raw_result.json()
        return json_result

    @classmethod
    def update(cls, request, options):
        json_encoded_request = cls.get_json_object(request)
        pki_string_request = cls.to_pki_request_string(request)
        raw_result = HttpClient.create().put(options['base_url'] + "/onboarding/submerchant",
                                              IyzipayResource.get_http_header(pki_string_request, options),
                                              json_encoded_request)
        json_result = raw_result.json()
        return json_result

    @classmethod
    def retrieve(cls, request, options):
        json_encoded_request = cls.get_json_object(request)
        pki_string_request = cls.to_pki_request_string(request)
        raw_result = HttpClient.create().post(options['base_url'] + "/onboarding/submerchant/detail",
                                              IyzipayResource.get_http_header(pki_string_request, options),
                                              json_encoded_request)
        json_result = raw_result.json()
        return json_result

    @classmethod
    def get_json_object(cls, request):
        json_object = JsonBuilder.from_json_object(super(SubMerchant, cls).get_json_object(request)) \
            .add("name", request.get('name', None))\
            .add("email", request.get('email', None))\
            .add("gsmNumber", request.get('gsm_number', None))\
            .add("address", request.get('address', None))\
            .add("iban", request.get('iban', None))\
            .add("taxOffice", request.get('tax_office', None))\
            .add("contactName", request.get('contact_name', None))\
            .add("contactSurname", request.get('contact_surname', None))\
            .add("legalCompanyTitle", request.get('legal_company_title', None))\
            .add("subMerchantExternalId", request.get('sub_merchant_external_id', None))\
            .add("subMerchantKey", request.get('sub_merchant_key', None))\
            .add("identityNumber", request.get('identity_number', None))\
            .add("taxNumber", request.get('tax_number', None))\
            .add("subMerchantType", request.get('sub_merchant_type', None))\
            .get_object()
        return JsonBuilder.json_encode(json_object)

    @classmethod
    def to_pki_request_string(cls, request):
        return RequestStringBuilder.create().append_super(
            super(SubMerchant, cls).to_pki_request_string(request)) \
            .append("name", request.get('name', None))\
            .append("email", request.get('email', None))\
            .append("gsmNumber", request.get('gsm_number', None))\
            .append("address", request.get('address', None))\
            .append("iban", request.get('iban', None))\
            .append("taxOffice", request.get('tax_office', None))\
            .append("contactName", request.get('contact_name', None))\
            .append("contactSurname", request.get('contact_surname', None))\
            .append("legalCompanyTitle", request.get('legal_company_title', None))\
            .append("subMerchantExternalId", request.get('sub_merchant_external_id', None))\
            .append("subMerchantKey", request.get('sub_merchant_key', None))\
            .append("identityNumber", request.get('identity_number', None))\
            .append("taxNumber", request.get('tax_number', None))\
            .append("subMerchantType", request.get('sub_merchant_type', None))\
            .get_request_string()