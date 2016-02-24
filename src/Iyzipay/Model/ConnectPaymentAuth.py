from src.Iyzipay.HttpClient import HttpClient
from src.Iyzipay.IyzipayResource import IyzipayResource
from src.Iyzipay.JsonBuilder import JsonBuilder
from src.Iyzipay.RequestStringBuilder import RequestStringBuilder


class ConnectPaymentAuth(IyzipayResource):
    @classmethod
    def create(cls, request, options):
        json_encoded_request = cls.get_json_object(request)
        pki_string_request = cls.to_pki_request_string(request)
        raw_result = HttpClient.create().post(options['base_url'] + "/payment/iyziconnect/auth",
                                              IyzipayResource.get_http_header(pki_string_request, options),
                                              json_encoded_request)
        json_result = raw_result.json()
        return json_result

    @classmethod
    def get_json_object(cls, request):
        json_object = JsonBuilder.from_json_object(super(ConnectPaymentAuth, cls).get_json_object(request)) \
            .add_price("price", request.get('price', None)) \
            .add_price("paidPrice", request.get('paid_price', None)) \
            .add("installment", request.get('installment', None)) \
            .add("buyerEmail", request.get('buyer_email', None)) \
            .add("buyerId", request.get('buyer_id', None)) \
            .add("buyerIp", request.get('buyer_ip', None)) \
            .add("posOrderId", request.get('pos_order_id', None)) \
            .add("paymentCard", cls.payment_card_get_json_object(request.get('payment_card', None))) \
            .add("connectorName", request.get('connector_name', None)) \
            .get_object()
        return JsonBuilder.json_encode(json_object)

    @classmethod
    def to_pki_request_string(cls, request):
        return RequestStringBuilder.create().append_super(
            super(ConnectPaymentAuth, cls).to_pki_request_string(request)) \
            .append_price("price", request.get('price', None)) \
            .append_price("paidPrice", request.get('paid_price', None)) \
            .append("installment", request.get('installment', None)) \
            .append("buyerEmail", request.get('buyer_email', None)) \
            .append("buyerId", request.get('buyer_id', None)) \
            .append("buyerIp", request.get('buyer_ip', None)) \
            .append("posOrderId", request.get('pos_order_id', None)) \
            .append("paymentCard", cls.payment_card_to_pki_request_string(request.get('payment_card', None))) \
            .append("connectorName", request.get('connector_name', None)) \
            .get_request_string()

    @classmethod
    def payment_card_get_json_object(cls, request):
        return JsonBuilder.create() \
            .add('cardHolderName', request.get('card_holder_name', None)) \
            .add('cardNumber', request.get('card_number', None)) \
            .add('expireYear', request.get('expire_year', None)) \
            .add('expireMonth', request.get('expire_month', None)) \
            .add('cvc', request.get('cvc', None)) \
            .add('registerCard', request.get('register_card', None)) \
            .add('cardAlias', request.get('card_alias', None)) \
            .add('cardToken', request.get('card_token', None)) \
            .add('cardUserKey', request.get('card_user_key', None)) \
            .get_object()

    @classmethod
    def payment_card_to_pki_request_string(cls, request):
        return RequestStringBuilder.create() \
            .append('cardHolderName', request.get('card_holder_name', None)) \
            .append('cardNumber', request.get('card_number', None)) \
            .append('expireYear', request.get('expire_year', None)) \
            .append('expireMonth', request.get('expire_month', None)) \
            .append('cvc', request.get('cvc', None)) \
            .append('registerCard', request.get('register_card', None)) \
            .append('cardAlias', request.get('card_alias', None)) \
            .append('cardToken', request.get('card_token', None)) \
            .append('cardUserKey', request.get('card_user_key', None)) \
            .get_request_string()
