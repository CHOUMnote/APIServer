from rest_framework.views import APIView, Response
from django.http import HttpResponse

import json

class MyAPI(APIView):
    def success(self, data=None):
        '''
        OK
        '''
        result = {
            "msg":"ok",
            "data":data
        }
        return HttpResponse(json.dumps(result), content_type = "application/json")
        # return Response(result)
    
    def error(self, msg=None):
        '''
        ERROR
        '''
        result = {
            "msg":"error",
            "data": msg
        }
        return Response(result)