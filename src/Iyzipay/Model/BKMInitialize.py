from src.Iyzipay.HttpClient import HttpClient
from src.Iyzipay.IyzipayResource import IyzipayResource
from src.Iyzipay.JsonBuilder import JsonBuilder
from src.Iyzipay.RequestStringBuilder import RequestStringBuilder


class BKMInitialize(IyzipayResource):
    @classmethod
    def create(cls, request, options):
        json_encoded_request = cls.get_json_object(request)
        pki_string_request = cls.to_pki_request_string(request)
        raw_result = HttpClient.create().post(options['base_url'] + "/payment/iyzipos/bkm/initialize/ecom",
                                              IyzipayResource.get_http_header(pki_string_request, options), json_encoded_request)
        json_result = raw_result.json()
        return json_result

    @classmethod
    def get_json_object(cls, request):
        json_object = JsonBuilder.from_json_object(super(BKMInitialize, cls).get_json_object(request)) \
            .add_price("price", request['price']) \
            .add("basketId", request['basket_id']) \
            .add("paymentGroup", request['payment_group']) \
            .add("buyer", request['buyer']) \
            .add("shippingAddress", request['shipping_address']) \
            .add("billingAddress", request['billing_address']) \
            .add_array("basketItems", request['basket_items']) \
            .add("callbackUrl", request['callback_url']) \
            .get_object()
        return JsonBuilder.json_encode(json_object)

    @classmethod
    def to_pki_request_string(cls, request):
        return RequestStringBuilder.create().append_super(super(BKMInitialize, cls).to_pki_request_string(request)) \
            .append_price("price", request['price']) \
            .append("basketId", request['basket_id']) \
            .append("paymentGroup", request['payment_group']) \
            .append("buyer", request['buyer']) \
            .append("shippingAddress", request['shipping_address']) \
            .append("billingAddress", request['billing_address']) \
            .append_array("basketItems", request['basket_items']) \
            .append("callbackUrl", request['callback_url']) \
            .get_request_string()
