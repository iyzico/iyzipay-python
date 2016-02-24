from src.Iyzipay.IyzipayResource import IyzipayResource
from src.Iyzipay.RequestFormatter import RequestFormatter


class RequestStringBuilder:
    def __init__(self, request_string):
        self.request_string = request_string

    @staticmethod
    def create():
        return RequestStringBuilder("")

    def append_super(self, superrequest_string):
        if superrequest_string is not None:
            superrequest_string = superrequest_string[1:-1]
            if superrequest_string is not None:
                self.request_string = self.request_string + superrequest_string + ","
        return self

    def append(self, key, value=None):
        if value:
            if isinstance(value, IyzipayResource):
                self.append_key_value(key, value.to_pki_request_string(value))
            else:
                self.append_key_value(key, value)
        return self

    def append_price(self, key, value=None):
        if value is not None and value is not "":
            self.append_key_value(key, RequestFormatter.format_price(value))
        return self

    def append_array(self, key, array=None):
        if array:
            appended_value = ""
            for value in array:
                if isinstance(value, dict):
                    appended_value = appended_value + value
                else:
                    appended_value = appended_value + value
                appended_value += ", "
            self.append_key_value_array(key, appended_value)
        return self

    def append_key_value(self, key, value=None):
        if value is not None and value is not "":
            self.request_string = self.request_string + key + "=" + str(value) + ","

    def remove_trailing_comma(self):
        self.request_string = self.request_string[:-1]
        return self

    def append_prefix(self):
        self.request_string = "[" + self.request_string + "]"
        return self

    def get_request_string(self):
        self.remove_trailing_comma()
        self.append_prefix()
        return self.request_string

    def append_key_value_array(self, key, appended_value):
        if appended_value:
            appended_value = appended_value[:-2]
            self.request_string = self.request_string + key + "=[" + appended_value + "],"
        return self
