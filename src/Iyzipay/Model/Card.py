from src.Iyzipay.HttpClient import HttpClient
from src.Iyzipay.IyzipayResource import IyzipayResource
from src.Iyzipay.JsonBuilder import JsonBuilder
from src.Iyzipay.RequestStringBuilder import RequestStringBuilder


class Card(IyzipayResource):
    @classmethod
    def create(cls, request, options):
        json_encoded_request = cls.get_json_object(request)
        pki_string_request = cls.to_pki_request_string(request)
        raw_result = HttpClient.create().post(options['base_url'] + "/cardstorage/card",
                                              IyzipayResource.get_http_header(pki_string_request, options),
                                              json_encoded_request)
        json_result = raw_result.json()
        return json_result

    @classmethod
    def delete(cls, request, options):
        json_encoded_request = cls.get_json_object(request)
        pki_string_request = cls.to_pki_request_string(request)
        raw_result = HttpClient.create().delete(options['base_url'] + "/cardstorage/card",
                                              IyzipayResource.get_http_header(pki_string_request, options),
                                              json_encoded_request)
        json_result = raw_result.json()
        return json_result

    @classmethod
    def get_json_object(cls, request):
        json_object = JsonBuilder.from_json_object(super(Card, cls).get_json_object(request)) \
            .add("externalId", request.get('external_id', None)) \
            .add("email", request.get('email', None)) \
            .add("cardUserKey", request.get('card_user_key', None))\
            .add("cardToken", request.get('card_token', None))\
            .add("card", cls.card_get_json_object(request.get('card', None))) \
            .get_object()
        return JsonBuilder.json_encode(json_object)

    @classmethod
    def to_pki_request_string(cls, request):
        return RequestStringBuilder.create().append_super(super(Card, cls).to_pki_request_string(request)) \
            .append("externalId", request.get('external_id', None)) \
            .append("email", request.get('email', None)) \
            .append('cardUserKey', request.get('card_user_key', None))\
            .append('cardToken', request.get('card_token', None))\
            .append("card", cls.card_to_pki_request_string(request.get('card', None))) \
            .get_request_string()

    @classmethod
    def card_get_json_object(cls, card):
        if card:
            return JsonBuilder.create()\
                .add('cardAlias', card.get('card_alias', None))\
                .add('cardNumber', card.get('card_number', None))\
                .add('expireYear', card.get('expire_year', None))\
                .add('expireMonth', card.get('expire_month', None))\
                .add('cardHolderName', card.get('card_holder_name', None))\
                .get_object()

    @classmethod
    def card_to_pki_request_string(cls, card):
        if card:
            return RequestStringBuilder.create()\
                .append('cardAlias', card.get('card_alias', None))\
                .append('cardNumber', card.get('card_number', None))\
                .append('expireYear', card.get('expire_year', None))\
                .append('expireMonth', card.get('expire_month', None))\
                .append('cardHolderName', card.get('card_holder_name', None))\
                .get_request_string()
