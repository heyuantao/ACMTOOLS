from django.contrib import admin
from django.conf.urls import  include, url
from django.conf import settings
from django.conf.urls.static import static

#from API.views import ContestListAPIView,
from API.views import UserAPIView
from HUSTOJ.views import AntiCheatingTaskContestListAPIView,AntiCheatingTaskContestRetriveUpdateAPIView
from MAIN.views import AntiCheatingMultiIPListAPIView,AntiCheatingMultiAccountListAPIView
from HUSTOJ.views import CodeExportTaskContestListAPIView,CodeExportTaskContestRetriveUpdateAPIView,CodeExportZipFileDownloadView
from API.views import LoginAPIView,LogoutAPIView

urlpatterns = [
    #url(r'^v1/contest/$', ContestListAPIView.as_view()),
    #url(r'^v1/user/$', HUSTOJUserListAPIView.as_view()),
    url(r'^v1/user/', UserAPIView.as_view()),
    url(r'^v1/login/', LoginAPIView.as_view()),
    url(r'^v1/logout/', LogoutAPIView.as_view()),

    url(r'^v1/anti_cheating_contest/(?P<contest_id>\d+)/multiip/', AntiCheatingMultiIPListAPIView.as_view()),
    url(r'^v1/anti_cheating_contest/(?P<contest_id>\d+)/multiaccount/', AntiCheatingMultiAccountListAPIView.as_view()),
    url(r'^v1/anti_cheating_contest/(?P<contest_id>\d+)/$', AntiCheatingTaskContestRetriveUpdateAPIView.as_view()),
    url(r'^v1/anti_cheating_contest/$', AntiCheatingTaskContestListAPIView.as_view()),


    url(r'^v1/code_export_contest/(?P<contest_id>\d+)/zip', CodeExportZipFileDownloadView.as_view()),
    url(r'^v1/code_export_contest/(?P<contest_id>\d+)/$', CodeExportTaskContestRetriveUpdateAPIView.as_view()),
    url(r'^v1/code_export_contest/', CodeExportTaskContestListAPIView.as_view()),
    ##################################
    #url(r'^v1/anticheatingtasktracking/$', AntiCheatingTaskTrackingListCreateAPIView.as_view()),
]

