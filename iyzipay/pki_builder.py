import base64

class PKIBuilder:
    def __init__(self, request_string):
        self.request_string = request_string

    def append(self, key, value=None):
        if value:
            self.append_key_value(key, value)
        return self

    def append_price(self, key, value=None):
        if value is not None and value is not "":
            self.append_key_value(key, str(round(float(value), 2)))
        return self

    def append_array(self, key, array=None):
        if array:
            appended_value = ""
            for value in array:
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


class IyziLink:
    def create(self,request):
        string = '{'
        if request.get('locale') is not None: string += '"locale":"'+request.get('locale')+'",'
        if request.get('conversationId') is not None: string += '"conversationId":"'+request.get('conversationId')+'",'
        if request.get('price') is not None: string += '"price":"'+request.get('price')+'",'
        if request.get('name') is not None: string += '"name":"'+request.get('name')+'",'
        if request.get('description') is not None: string += '"description":"'+request.get('description')+'",'
        if request.get('encodedImageFile') is not None:
            encoded_string = False
            with open(request.get('encodedImageFile'), "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
            string += '"encodedImageFile":"'+encoded_string.decode('utf-8')+'",'
        if request.get('currencyCode') is not None: string += '"currencyCode":"'+request.get('currencyCode')+'",'
        if request.get('addressIgnorable') is not None: string += '"addressIgnorable":'+str(int(request.get('addressIgnorable')))+','
        if request.get('stockEnabled') is not None: string += '"stockEnabled":'+str(int(request.get('stockEnabled')))+','
        if request.get('stockCount') is not None: string += '"stockCount":'+str(request.get('stockCount'))+','
        if request.get('soldLimit') is not None: string += '"soldLimit":'+str(int(request.get('soldLimit')))+','
        if request.get('installmentRequested') is not None: string += '"installmentRequested":'+str(int(request.get('installmentRequested')))+''
        string += '}'
        return string

    def delete(self,request):
        string = '{'
        if request.get('locale') is not None: string += '"locale":"'+request.get('locale')+'",'
        if request.get('conversationId') is not None: string += '"conversationId":"'+request.get('conversationId')+'",'
        if request.get('token') is not None: string += '"token":"'+request.get('token')+'"'
        string += '}'
        return string

    def to_string(self,url,request):
        if request.get('conversationId') is not None:
            url = url + '?conversationId='+request.get('conversationId')
        if request.get('locale') is not None:
            if (url.find('?') != -1):
                 url = url+"&locale="+request.get('locale')
            else:
                 url = url+"?locale="+request.get('locale')
        if request.get('page') is not None:
            url = url+"&page="+str(request.get('page'))
        if request.get('count') is not None:
            url = url+"&count="+str(request.get('count'))
        return url

    def update(self,request):
        return self.create(request)