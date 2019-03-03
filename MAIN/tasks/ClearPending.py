# -*- coding: utf-8 -*-
import django
django.setup()
from django.conf import settings
from HUSTOJ.models import Solution,Contest,SourceCode,ContestProblem
from MAIN.models import TaskTracking
from celery.task import Task
from datetime import datetime
from celery.task import PeriodicTask
from celery.signals import celeryd_init
import shutil
import os
import time
import zipfile
import traceback

class ClearPendingTask(Task):
    task_name = 'clear_pending_task'
    def run(self):
        print("Task :{} started !".format(self.task_name))
        task_tracking_query_set = TaskTracking.objects.filter(status='pending')
        for one_task in task_tracking_query_set:
            one_task.status='error'
            one_task.save()
        print("Task :{} end !".format(self.task_name))

#@celeryd_init.connect(sender=None)
#def configure_worker12(conf=None, **kwargs):
#    print("####################################")