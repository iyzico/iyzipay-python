import pprint

import requests


class HttpClient:
    @staticmethod
    def create():
        return HttpClient()

    def get(self, url, header):
        req = requests.get(url, headers=header, verify=True)
        return req

    def post(self, url, header, content):
        req = requests.post(url, headers=header, data=content, verify=True)
        return req

    def put(self, url, header, content):
        req = requests.put(url, headers=header, data=content, verify=True)
        return req

    def delete(self, url, header, content=None):
        req = requests.delete(url, headers=header, data=content, verify=True)
        return req
