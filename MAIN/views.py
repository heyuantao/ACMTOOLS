from __future__ import unicode_literals
from django.views.generic.base import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
#from django.template.context import RequestContext
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from MAIN.paginations import CustomItemPagination
from django.template import RequestContext
from django.http.response import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from MAIN.models import MultiIPAnalyze,MultiAccountAnalyze
from MAIN.serializers import MultiIPAnalyzeSerializer,MultiAccountAnalyzeSerializer
import traceback
import logging



logger = logging.getLogger(__name__)

# Create your views here.

class TestLoginView(View):
    template = 'testLoginAndLogout.html'
    def get(self,request):
        pageContext = request.GET.dict()
        return render(request, self.template, pageContext)
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        pageContext = request.GET.dict()
        if user is not None and user.is_active:
            login(request, user)
            return render(request, self.template, pageContext)
        else:
            return render(request, self.template, pageContext)

class TestLogoutView(View):
    template = 'testLoginAndLogout.html'
    def get(self,request):
        logout(request)
        pageContext = request.GET.dict()
        return HttpResponseRedirect("/main/testlogin")

class AntiCheatingMultiIPListAPIView(generics.ListAPIView):

    serializer_class = MultiIPAnalyzeSerializer
    pagination_class = CustomItemPagination

    def get_queryset(self):
        queryset = MultiIPAnalyze.objects.filter(contest_id=self.contest_id)
        return queryset

    def list(self,request,*args,**kwargs):
        self.contest_id = kwargs['contest_id'];
        return  super().list(request,*args,**kwargs)

class AntiCheatingMultiAccountListAPIView(generics.ListAPIView):

    serializer_class = MultiAccountAnalyzeSerializer
    pagination_class = CustomItemPagination

    def get_queryset(self):
        queryset = MultiAccountAnalyze.objects.filter(contest_id=self.contest_id)
        return queryset

    def list(self,request,*args,**kwargs):
        self.contest_id = kwargs['contest_id'];
        return  super().list(request,*args,**kwargs)