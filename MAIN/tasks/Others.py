from celery.task import Task
import time

class HelpTask(Task):
    name = 'help_task'
    def run(self,*args,**kwargs):
        print('start course task')
        time.sleep(10)
        print(kwargs)
        #runTask(1000)
        print('end')