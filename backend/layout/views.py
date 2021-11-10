from django.shortcuts import render
from rest_framework import serializers

######################################
    ### Rest Framework Imports ###
######################################
from rest_framework.views import APIView
from rest_framework.response import Response
######################################
    ### Serializers and Models ###
######################################
from .serializers import TableSerializer
from .models import Computers, Tables

class LayoutView(APIView):
    def get(self, request, format=None):
        computers = Tables.objects.all()[0:4]
        serializer = TableSerializer(computers, many=True)
        return Response(serializer.data)


