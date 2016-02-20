class IyzipayResourceMapper:
    @staticmethod
    def new_instance():
        return IyzipayResourceMapper()

    def map_response(self, response, json_result):

        if "status" in json_result.keys():
            response['status'] = json_result['status']

        if "conversationId" in json_result.keys():
            response['conversation_id'] = json_result['conversationId']

        if "errorCode" in json_result.keys():
            response['error_code'] = json_result['errorCode']

        if "errorMessage" in json_result.keys():
            response['error_message'] = json_result['errorMessage']

        if "errorGroup" in json_result.keys():
            response['error_group'] = json_result['errorGroup']

        if "locale" in json_result.keys():
            response['locale'] = json_result['locale']

        if "systemTime" in json_result.keys():
            response['system_time'] = json_result['systemTime']
