# -*- coding: utf-8 -*-
import django
django.setup()
from django.conf import settings
from HUSTOJ.models import Solution,Contest,SourceCode,ContestProblem
from MAIN.models import TaskTracking
from celery.task import Task
from datetime import datetime
import pandas as pd
import shutil
import os
import logging
import traceback

logger = logging.getLogger(__name__)

DATABSENAME = 'hustoj'
TOPDIRECTORY = os.path.join(settings.MEDIA_ROOT,'export')


class CodeExportExporter:

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

    def getContestProblemIdList(self):
        contest_query_set = ContestProblem.objects.using(DATABSENAME).filter(contest_id=self.contest_id)
        problem_list = list( set(contest_query_set.values_list('problem_id',flat=True)) )
        return problem_list

    def getUserList(self):
        solution_query_set = Solution.objects.using(DATABSENAME).filter(contest_id=self.contest_id).exclude(user_id='admin')
        user_id_list = list( set(solution_query_set.values_list('user_id',flat=True ) ) )
        return user_id_list

    def getSolutionIdListInContestOfUser(self,contest_id,user_id):
        solution_query_set = Solution.objects.using(DATABSENAME).filter(user_id=user_id).filter(contest_id=self.contest_id).\
            filter(result=4)
        solution_id_list = list( set(solution_query_set.values_list('solution_id',flat=True )) )
        return solution_id_list

    def getCodeOfSolutionId(self,solution_id):
        sourcecode_query_set = SourceCode.objects.using(DATABSENAME).filter(solution_id=solution_id)
        if sourcecode_query_set:
            sourcecode_instance = sourcecode_query_set[0]
            source_code = sourcecode_instance.source
        else:
            source_code = ""
        return source_code

    def getSolutionIdInContestOfUserByProbmemId(self,contest_id,user_id,problem_id):
        solution_query_set = Solution.objects.using(DATABSENAME).filter(user_id=user_id).\
            filter(contest_id=self.contest_id).filter(problem_id=problem_id).\
            filter(result=4)
        if solution_query_set:
            return solution_query_set[0].solution_id
        else:
            return None

    def getSolutionIdInContestByProbmemAndUser(self,contest_id,problem_id,user_id):
        solution_query_set = Solution.objects.using(DATABSENAME).filter(user_id=user_id). \
            filter(contest_id=self.contest_id).filter(problem_id=problem_id). \
            filter(result=4)
        if solution_query_set:
            return solution_query_set[0].solution_id
        else:
            return -1

    def getContestResultDataFrame(self):
        user_id_list = self.getUserList()
        problem_id_list = self.getContestProblemIdList()
        result_list = []
        for one_user_id in user_id_list:
            one_row_dict_in_result_list = {}
            one_row_dict_in_result_list['user_id']=one_user_id
            for one_problem_id in problem_id_list:
                one_solution_id = self.getSolutionIdInContestByProbmemAndUser(self.contest_id,one_problem_id,one_user_id)
                one_row_dict_in_result_list[one_problem_id]=one_solution_id
            result_list.append(one_row_dict_in_result_list)
        result_pd = pd.DataFrame.from_dict(result_list)
        return result_pd

    def run(self):
        contest_directory = os.path.join(TOPDIRECTORY,str(self.contest_id))
        contest_directory_zip_file = "{}.zip".format(contest_directory)
        if os.path.exists(contest_directory):
            shutil.rmtree(contest_directory)
        if os.path.exists(contest_directory_zip_file):
            os.remove(contest_directory_zip_file)
        os.mkdir(contest_directory)
        ######################################

        user_list = self.getUserList()
        contset_problem_id = self.getContestProblemIdList()
        for one_user_id in user_list:
            user_directory_in_contest = os.path.join(TOPDIRECTORY, str(self.contest_id), str(one_user_id))
            os.mkdir(user_directory_in_contest)
            for problem_id in contset_problem_id:
                one_solution_id = self.getSolutionIdInContestOfUserByProbmemId(self.contest_id,one_user_id,problem_id)
                if one_user_id:
                    source_code = self.getCodeOfSolutionId(one_solution_id)
                else:
                    source_code = ''
                file_name = os.path.join(user_directory_in_contest,"{}.c".format(problem_id))
                with open(file_name,'w',encoding='utf-8') as file:
                    file.write(source_code)
        ######################################
        #generate result csv
        contest_csv_file = os.path.join(TOPDIRECTORY,str(self.contest_id), "{}.csv".format(self.contest_id))
        df = self.getContestResultDataFrame()
        df.to_csv(contest_csv_file)
        ######################################
        #zip and delete dir
        shutil.make_archive(contest_directory, 'zip', contest_directory)
        if os.path.exists(contest_directory):
            shutil.rmtree(contest_directory)


class CodeExportTask(Task):
    task_name = 'code_export_task'
    def run(self,contest_id):
        self.contest_id = int(contest_id)
        print('Start code_export_task Task')
        code_exporter = CodeExportExporter(self.contest_id)
        task_tracking_query_set = TaskTracking.objects.filter(task_name=self.task_name,contest_id=self.contest_id)
        if task_tracking_query_set:
            task_tracking_instance = task_tracking_query_set[0]
            task_tracking_instance.in_date = datetime.now()
            task_tracking_instance.status = 'pending'
            task_tracking_instance.save()
        else:
            task_tracking_instance = TaskTracking.objects.create(task_name=self.task_name, contest_id=self.contest_id,
                                                                in_date=datetime.now(), status='pending')
        #########################Task run ###############################
        try:
            code_exporter.run()
        except Exception as error:
            logger.exception(error)
            task_tracking_instance.status = 'error'
            task_tracking_instance.save()
            traceback.print_exc()
        finally:
            task_tracking_instance.status = 'finished'
            task_tracking_instance.save()
            print('code_export_task Finished')