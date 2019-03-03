from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from HUSTOJ.models import Contest,Users
from HUSTOJ.serializers import ContestSerializer,HUSTOJUserSerializer
from MAIN.models import TaskTracking
from MAIN.serializers import UserSerializer
from MAIN.paginations import CustomItemPagination
from MAIN.tasks.AntiCheating import AntiCheatingTask
import traceback

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
            response = Response({"redirect_url": "login"}, status=302)
            response['Cache-Control'] = 'no-cache'
            return response

    def post(self, request, format=None):  #系统用该接口查询用户信息，其实不怎么合适，应当放在get函数里
        return Response({"error_message": u"该接口未启用"}, status=404)

    def put(self, request, format=None):
        user = request.user
        if user.is_authenticated():
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                userInstance = serializer.save()
                return Response(serializer.data, status=200)
        else:
            response = Response({"redirect_url": "none"}, status=302)
            response['Cache-Control'] = 'no-cache'
            return response

class LoginAPIView(APIView):

    def get(self, request, format=None):
        if request.user.is_authenticated():
            return Response({"message": request.user }, status=200)
        else:
            return Response({"message": "Not login !"}, status=200)

    def post(self, request, format=None):
        emailString = request.data.get("email")
        passwordString = request.data.get("password")
        user = authenticate(username=emailString, password=passwordString)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return Response({"dashboard_url": reverse("manager")}, status=200)
        else:
            return Response({"error_message": "用户名或密码错误 !"}, status=400)

class LogoutAPIView(APIView):
    def get(self, request, format=None):
        return Response({"erro_message": u"该接口未启用"}, status=404)
    def post(self, request, format=None):
        try:
            logout(request)
            return Response({"redirect_url": reverse("login")}, status=302)
        except Exception as e:
            estring = traceback.format_exc()
            logger.error(estring)
            return Response({u"error_message": u"程序发生异常"}, status=400)
        #return Response({"errormessage": u"该接口未启用"}, status=400)
