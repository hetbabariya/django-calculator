from datetime import date
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class calcOperation(APIView):
    
    def post(self , request):
        data = request.data

        try:
            result = eval(data.get('data'))
            return Response({"Result" : result})
        except Exception as e:
            return Response({"message":str(e)})

        


