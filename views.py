from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from argus.models import Logdb
from argus.serializers import Logserializer

@api_view(["get"])
def log_info(request):
    logs = Logdb.objects.all()
    serializer_class = Logserializer(logs, many=True)
    return Response(serializer_class.data, status=status.HTTP_200_OK,)