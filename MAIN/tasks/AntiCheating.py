# -*- coding: utf-8 -*-
import django
django.setup()
from HUSTOJ.models import Solution,Contest,Loginlog,Users
from MAIN.models import MultiIPAnalyze,MultiIPAnalyzeRecord
from MAIN.models import MultiAccountAnalyze,MultiAccountAnalyzeRecord
from MAIN.models import TaskTracking
from celery.task import Task
from datetime import datetime
import logging
import traceback

logger = logging.getLogger(__name__)

DATABSENAME = 'hustoj'

class OneAccountWithMultiIPChecker:

    def __init__(self,contest_id):
        self.contest_id = int(contest_id)

    def getContestTitle(self):
        if hasattr(self,'contest_title'):
            return self.contest_title
        contest_id = self.contest_id
        query_set = Contest.objects.using(DATABSENAME).filter(contest_id=contest_id)
        if query_set:
            self.contest_title = query_set[0].title
        else:
            self.contest_title = ""
        return self.contest_title

    def clearLatestResult(self):
        query_set = MultiIPAnalyze.objects.filter(contest_id=self.contest_id)
        for item in query_set:
            item.records.all().delete()
            item.delete()

    def getUserQuerySet(self):
        if hasattr(self,'user_id_list'):
            return self.user_id_list
        contest_id = self.contest_id
        self.user_id_list =  Solution.objects.using(DATABSENAME).filter(contest_id=contest_id).exclude(user_id='admin').\
            values_list('user_id',flat=True).distinct()
        return self.user_id_list

    def getUserLoginIP(self,user_id):
        pass

    def getUserNickname(self,user_id):
        user_query_set = Users.objects.using(DATABSENAME).filter(user_id=user_id)
        if user_query_set:
            return user_query_set[0].nick
        else:
            return ''

    def getUserSubmitQuerySet(self,user_id):
        solution_query_set = Solution.objects.using(DATABSENAME).filter(contest_id=self.contest_id).filter(user_id=user_id).\
            values('ip','in_date')
        return solution_query_set

    def checkContestExist(self):
        contest_id = self.contest_id
        contest_query_set = Contest.objects.using(DATABSENAME).filter(contest_id=contest_id)
        if contest_query_set:
            return True
        else:
            return False

    def run(self):
        if not self.checkContestExist():
            return
        user_query_set = self.getUserQuerySet()
        for one_user in user_query_set:
            submit_query_set = self.getUserSubmitQuerySet(one_user)
            analyze_instance,_ = MultiIPAnalyze.objects.\
                get_or_create(contest_id=self.contest_id,contest_title=self.getContestTitle(),\
                              account_id=one_user,account_nick=self.getUserNickname(one_user) )
            analyze_instance.save()
            for item in submit_query_set:
                MultiIPAnalyzeRecord.objects.create(ip=item['ip'],in_date=item['in_date'],record=analyze_instance).save()
            analyze_instance.status = 'finished'
            analyze_instance.save()



class OneIPWithMultiAccountChecker:

    def __init__(self,contest_id):
        self.contest_id = int(contest_id)

    def getIpQuerySet(self):
        if hasattr(self,'ip_list'):
            return self.ip_list
        contest_id = self.contest_id
        self.ip_list =  Solution.objects.using(DATABSENAME).filter(contest_id=contest_id).exclude(user_id='admin').\
            values_list('ip',flat=True).distinct()
        return self.ip_list

    def getContestTitle(self):
        if hasattr(self,'contest_title'):
            return self.contest_title
        contest_id = self.contest_id
        query_set = Contest.objects.using(DATABSENAME).filter(contest_id=contest_id)
        if query_set:
            self.contest_title = query_set[0].title
        else:
            self.contest_title = ""
        return self.contest_title

    def getUserNickname(self,user_id):
        user_query_set = Users.objects.using(DATABSENAME).filter(user_id=user_id)
        if user_query_set:
            return user_query_set[0].nick
        else:
            return ''

    def getUserSubmitQuerySet(self,ip):
        solution_query_set = Solution.objects.using(DATABSENAME).filter(contest_id=self.contest_id).filter(ip=ip).\
            values('user_id','in_date')
        return solution_query_set

    def checkContestExist(self):
        contest_id = self.contest_id
        contest_query_set = Contest.objects.using(DATABSENAME).filter(contest_id=contest_id)
        if contest_query_set:
            return True
        else:
            return False

    def clearLatestResult(self):
        query_set = MultiAccountAnalyze.objects.filter(contest_id=self.contest_id)
        for item in query_set:
            item.records.all().delete()
            item.delete()

    def run(self):
        if not self.checkContestExist():
            return

        ip_query_set = self.getIpQuerySet()
        for one_ip in ip_query_set:
            submit_query_set = self.getUserSubmitQuerySet(one_ip)
            analyze_instance, _ = MultiAccountAnalyze.objects. \
                get_or_create(contest_id=self.contest_id, contest_title=self.getContestTitle(), \
                              ip=one_ip)
            analyze_instance.save()
            for item in submit_query_set:
                MultiAccountAnalyzeRecord.objects.create(account_id=item['user_id'],account_nick=self.getUserNickname(item['user_id']),\
                                                         in_date=item['in_date'],\
                                                         record=analyze_instance).save()
            analyze_instance.status = 'finished'
            analyze_instance.save()


class AntiCheatingTask(Task):
    task_name = 'anti_cheating_task'

    def checkContestExist(self,contest_id):
        contest_query_set = Contest.objects.using(DATABSENAME).filter(contest_id=contest_id)
        if contest_query_set:
            return True
        else:
            return False

    def run(self,contest_id):

        self.contest_id = int(contest_id)
        if not self.checkContestExist(self.contest_id):
            print("Contest ID Not Exist !")
            return
        print('Start AntiCheatingTask !')
        checker_first = OneAccountWithMultiIPChecker(self.contest_id)
        checker_second = OneIPWithMultiAccountChecker(self.contest_id)
        checker_task_tracking_query_set = TaskTracking.objects.filter(task_name=self.task_name, contest_id=self.contest_id)
        if checker_task_tracking_query_set:
            checker_task_tracking = checker_task_tracking_query_set[0]
            checker_task_tracking.in_date = datetime.now()
            checker_task_tracking.status = 'pending'
            checker_task_tracking.save()
            # do not recalc if prev task is runing
            #if TaskTracking.objects.get(task_name=self.task_name, contest_id=self.contest_id).status == 'pending':
            #    return
        else:
            checker_task_tracking = TaskTracking.objects.create(task_name=self.task_name, contest_id=self.contest_id,in_date=datetime.now(), status='pending')
        #####################################
        try:
            checker_first.clearLatestResult()
            checker_first.run()
            checker_second.clearLatestResult()
            checker_second.run()
            checker_task_tracking.status='finished'
            checker_task_tracking.in_date = datetime.now()
        except Exception as error:
            logger.exception(error)
            checker_task_tracking.status='error'
            checker_task_tracking.in_date = datetime.now()
        finally:
            checker_task_tracking.save()
            print('AntiCheatingTask Finished !')
