from django.contrib import admin
from django.conf.urls import  include, url
from django.conf import settings
from django.conf.urls.static import static
from MAIN.views import TestLoginView, TestLogoutView,LoginView,ManagerView,IndexView
import os

LOGIN_MEDIA_ROOT = os.path.join(settings.MEDIA_ROOT, 'login/build/')
LOGIN_MEDIA_URL = "login/media/"
MANAGER_MEDIA_ROOT = os.path.join(settings.MEDIA_ROOT, 'manager/build/')
MANAGER_MEDIA_URL = "manager/media/"


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'loginandregistration$', LoginView.as_view(), name='login'),
    url(r'manager$', ManagerView.as_view(), name='manager'),

    url(r'testlogin$', TestLoginView.as_view(), name='testlogin'),
    url(r'testlogout$', TestLogoutView.as_view(), name='testlogout'),
] + static(MANAGER_MEDIA_URL, document_root=MANAGER_MEDIA_ROOT) \
  + static(LOGIN_MEDIA_URL, document_root=LOGIN_MEDIA_ROOT)


#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
