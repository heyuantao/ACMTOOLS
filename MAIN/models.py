from django.db import models
#from celery.signals import celeryd_init

# Create your models here.

#for ip on same account

class TaskTracking(models.Model):
    task_status_list = ['pending','fnished','error']  #show the task status
    task_name = models.CharField(max_length=50)
    contest_id = models.IntegerField()
    in_date = models.DateTimeField()
    status = models.CharField(max_length=10)  # in task_stats_list


#########################################################
class MultiIPAnalyze(models.Model):
    contest_id = models.IntegerField()
    contest_title = models.CharField(max_length=255,null=True)
    account_id = models.CharField(max_length=48)  #the user name\
    account_nick = models.CharField(max_length=100,null=True)  # the user nick
    #status = models.CharField(max_length=70)  # 'pending' or 'finshed'

class MultiIPAnalyzeRecord(models.Model):
    ip = models.CharField(max_length=70)
    in_date = models.DateTimeField()
    record = models.ForeignKey(MultiIPAnalyze,related_name='records')
#############################################################

#for multi account on same ip
############################################################
class MultiAccountAnalyze(models.Model):
    contest_id = models.IntegerField()
    contest_title = models.CharField(max_length=255,null=True)
    ip = models.CharField(max_length=70)
    #status = models.CharField(max_length=70)  # 'pending' or 'finshed'

class MultiAccountAnalyzeRecord(models.Model):
    account_id = models.CharField(max_length=48)
    account_nick = models.CharField(max_length=100,null=True)  # the user nick
    in_date = models.DateTimeField()
    record = models.ForeignKey(MultiAccountAnalyze,related_name='records')
####################################################################