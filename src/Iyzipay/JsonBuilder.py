import json

from src.Iyzipay.IyzipayResource import IyzipayResource
from src.Iyzipay.RequestFormatter import RequestFormatter


class JsonBuilder:
    def __init__(self, json=None):
        self.json = json
        self.value = ""

    @staticmethod
    def create():
        return JsonBuilder({})

    @staticmethod
    def from_json_object(json):
        return JsonBuilder(json)

    def add(self, key, value=None):
        if value:
            if isinstance(value, IyzipayResource):
                self.json[key] = value.get_json_object(value)
            else:
                self.json[key] = value
        return self

    def add_price(self, key, value=None):
        if value:
            self.json.update({key: RequestFormatter.format_price(value)})
        return self

    def add_array(self, key, array=None):
        if array:
            self.json[key] = []
            for index, value in enumerate(array):
                if isinstance(value, IyzipayResource):
                    self.json[key].append(value.get_json_object(value))
                else:
                    self.json[key].append(value)
        return self

    def get_object(self):
        return self.json

    @staticmethod
    def json_encode(json_object):
        return json.dumps(json_object)
