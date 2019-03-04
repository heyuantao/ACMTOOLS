from django.views.generic.base import View
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from MAIN.paginations import CustomItemPagination
from MAIN.models import TaskTracking
from django.conf import settings
from HUSTOJ.models import Contest
from HUSTOJ.serializers import AntiCheatingTaskContestSerializer,CodeExportTaskContestSerializer
from datetime import datetime
from MAIN.tasks.AntiCheating import AntiCheatingTask
from MAIN.tasks.CodeExport import CodeExportTask
import logging
import os

logger = logging.getLogger(__name__)
DATABSENAME = 'hustoj'

# Create your views here.

class AntiCheatingTaskContestListAPIView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset =  Contest.objects.using(DATABSENAME).all()
    serializer_class = AntiCheatingTaskContestSerializer
    pagination_class = CustomItemPagination

#When update ，no change the hustoj db ,only update task record in MAIN models
class AntiCheatingTaskContestRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Contest.objects.using(DATABSENAME).all()
    serializer_class = AntiCheatingTaskContestSerializer
    pagination_class = CustomItemPagination
    def retrieve(self, request, *args, **kwargs):
        try:
            contest_id = kwargs['contest_id']
            instance = self.get_queryset().get(contest_id=contest_id)
            seralizer_class = self.get_serializer_class()
            seralizer = seralizer_class(instance)
            return Response(seralizer.data, status=200)
        except Exception:
            return Response({}, status=400)

    def update(self, request, *args, **kwargs):
        try:
            contest_id = kwargs['contest_id']
            query_set = TaskTracking.objects.filter(task_name=AntiCheatingTask.task_name).filter(contest_id=contest_id)
            if not query_set:
                instance = TaskTracking.objects.create(task_name=AntiCheatingTask.task_name,contest_id=contest_id,in_date=datetime.now(),status='pending')
            else:
                instance = query_set[0]
                if instance.status == 'pending':
                    raise Exception('In pending !')
                instance.status = 'pending'
                instance.save()
            AntiCheatingTask.delay(int(contest_id))
            return Response({},status=200)
        except Exception:
            return Response({}, status=400)

class CodeExportTaskContestListAPIView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset =  Contest.objects.using(DATABSENAME).all()
    serializer_class = CodeExportTaskContestSerializer
    pagination_class = CustomItemPagination

class CodeExportTaskContestRetriveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Contest.objects.using(DATABSENAME).all()
    serializer_class = CodeExportTaskContestSerializer
    pagination_class = CustomItemPagination
    def retrieve(self, request, *args, **kwargs):
        try:
            contest_id = kwargs['contest_id']
            instance = self.get_queryset().get(contest_id=contest_id)
            seralizer_class = self.get_serializer_class()
            seralizer = seralizer_class(instance)
            return Response(seralizer.data, status=200)
        except Exception:
            return Response({}, status=400)
    def update(self, request, *args, **kwargs):
        try:
            contest_id = kwargs['contest_id']
            query_set = TaskTracking.objects.filter(task_name=CodeExportTask.task_name).filter(contest_id=contest_id)
            if not query_set:
                instance = TaskTracking.objects.create(task_name=CodeExportTask.task_name,contest_id=contest_id,in_date=datetime.now(),status='pending')
            else:
                instance = query_set[0]
                if instance.status == 'pending':
                    raise Exception('In pending !')
                instance.status = 'pending'
                instance.save()
            CodeExportTask.delay(int(contest_id))
            return Response({},status=200)
        except Exception:
            return Response({}, status=400)

class CodeExportZipFileDownloadView(View):
    TOPDIRECTORY = os.path.join(settings.MEDIA_ROOT, 'export')
    def checkHasPermission(self,request):
        if request.is_superuser:
            return True
        return False
    def get(self,request,*args,**kwargs):
        try:
            if not self.checkHasPermission():
                raise Exception("You not has permission in CodeExportZipFileDownloadView Class !")

            contest_id = kwargs['contest_id']
            export_zip_file_path = "{}.zip".format( os.path.join(self.TOPDIRECTORY,contest_id) )
            with open(export_zip_file_path, 'rb') as file:
                response = HttpResponse(file)
                response['content_type']='application/octet-stream'
                response['Content-Disposition'] = 'attachment; filename="code.zip"'
                return response

        except Exception:
            return Response({}, status=400)