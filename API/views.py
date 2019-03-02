from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from HUSTOJ.models import Contest,Users
from HUSTOJ.serializers import ContestSerializer,HUSTOJUserSerializer
from MAIN.models import TaskTracking
from MAIN.serializers import UserSerializer
from MAIN.paginations import CustomItemPagination
from MAIN.tasks.AntiCheating import AntiCheatingTask

import logging

logger = logging.getLogger(__name__)
DATABSENAME = 'hustoj'
# Create your views here.


class UserAPIView(APIView):  #This class handle user information retrive and update some part of user information,such as address ,email etc
    def get(self, request, format=None):
        userInstance = request.user
        if userInstance.is_authenticated():
            serializer = UserSerializer(userInstance)
            return Response(serializer.data, status=200)
        else:
            #response = Response({"redirecturl": reverse("loginandregistration")}, status=302)
            response = Response({"redirecturl": "login"}, status=302)
            response['Cache-Control'] = 'no-cache'
            return response

    def post(self, request, format=None):  #系统用该接口查询用户信息，其实不怎么合适，应当放在get函数里
        return Response({"errormessage": u"该接口未启用"}, status=404)
        #userInstance = request.user
        #if userInstance.is_authenticated():
        #    #userInstance = User.objects.get(email="hyt@163.com")
        #    serializer = UserSerializer(userInstance)
        #    return Response(serializer.data, status=200)
        #else:
        #    return Response({"redirecturl": reverse("loginandregistration")}, status=302)

    def put(self, request, format=None):
        user = request.user
        if user.is_authenticated():
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                userInstance = serializer.save()
                return Response(serializer.data, status=200)
        else:
            response = Response({"redirecturl": "none"}, status=302)
            response['Cache-Control'] = 'no-cache'
            return response

