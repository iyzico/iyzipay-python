import base64

from src.Iyzipay.HttpClient import HttpClient
from src.Iyzipay.IyzipayResource import IyzipayResource
from src.Iyzipay.JsonBuilder import JsonBuilder
from src.Iyzipay.RequestStringBuilder import RequestStringBuilder


class ConnectBKMInitialize(IyzipayResource):
    @classmethod
    def create(cls, request, options):
        json_encoded_request = cls.get_json_object(request)
        pki_string_request = cls.to_pki_request_string(request)
        raw_result = HttpClient.create().post(options['base_url'] + "/payment/iyziconnect/bkm/initialize",
                                              IyzipayResource.get_http_header(pki_string_request, options),
                                              json_encoded_request)
        json_result = raw_result.json()
        json_result['htmlContent'] = base64.b64decode(json_result['htmlContent'])
        return json_result

    @classmethod
    def get_json_object(cls, request):
        json_object = JsonBuilder.from_json_object(super(ConnectBKMInitialize, cls).get_json_object(request)) \
            .add("connectorName", request.get('connector_name', None)) \
            .add_price("price", request.get('price', None)) \
            .add("callbackUrl", request.get('callback_url', None)) \
            .add("buyerEmail", request.get('buyer_email', None)) \
            .add("buyerId", request.get('buyer_id', None)) \
            .add("buyerIp", request.get('buyer_ip', None)) \
            .add("posOrderId", request.get('pos_order_id', None)) \
            .add("installmentDetails",
                 cls.installment_details_get_json_object(request.get('installment_details', None))) \
            .get_object()
        return JsonBuilder.json_encode(json_object)

    @classmethod
    def to_pki_request_string(cls, request):
        return RequestStringBuilder.create().append_super(
            super(ConnectBKMInitialize, cls).to_pki_request_string(request)) \
            .append("connectorName", request.get('connector_name', None)) \
            .append_price("price", request.get('price', None)) \
            .append("callbackUrl", request.get('callback_url', None)) \
            .append("buyerEmail", request.get('buyer_email', None)) \
            .append("buyerId", request.get('buyer_id', None)) \
            .append("buyerIp", request.get('buyer_ip', None)) \
            .append("posOrderId", request.get('pos_order_id', None)) \
            .append("installmentDetails",
                    cls.installment_details_to_pki_request_string(request.get('installment_details', None))) \
            .get_request_string()

    @classmethod
    def installment_details_to_pki_request_string(cls, installment_details):
        installment = []
        for installment_detail in installment_details:
            installment.append(RequestStringBuilder.create() \
                               .append('bankId', installment_detail.get('bank_id', None)) \
                               .append('installmentPrices', cls.installment_prices_to_pki_request_string(
                installment_detail.get('installment_prices', None))) \
                               .get_request_string())
        return '[' + ", ".join(installment) + ']'

    @classmethod
    def installment_details_get_json_object(cls, installment_details):
        installment = []
        for installment_detail in installment_details:
            installment.append(JsonBuilder.create() \
                               .add('bankId', installment_detail.get('bank_id', None))
                               .add('installmentPrices', cls.installment_prices_get_json_object(
                installment_detail.get('installment_prices', None)))
                               .get_object())
        return installment

    @classmethod
    def installment_prices_to_pki_request_string(cls, installment_prices):
        prices = []
        for installment_price in installment_prices:
            prices.append(RequestStringBuilder.create() \
                          .append('installmentNumber', installment_price.get('installment_number', None))
                          .append_price('totalPrice', installment_price.get('total_price', None))
                          .get_request_string())

        return '[' + ", ".join(prices) + ']'

    @classmethod
    def installment_prices_get_json_object(cls, installment_prices):
        prices = []
        for installment_price in installment_prices:
            prices.append(JsonBuilder.create()
                          .add('installmentNumber', installment_price.get('installment_number', None))
                          .add_price('totalPrice', installment_price.get('total_price', None))
                          .get_object())
        return prices
