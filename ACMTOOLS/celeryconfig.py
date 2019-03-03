import djcelery
from celery import Celery, platforms

djcelery.setup_loader()

CELERY_IMPORTS = (
    'MAIN.tasks.AntiCheating',
    'MAIN.tasks.CodeExport',
    'MAIN.tasks.ClearPending'
)

#this could enable celery run in root mode under supervisor
platforms.C_FORCE_ROOT = True

CELERYD_FORCE_EXECV =True

CELERYD_CONCURRENCY = 1

CELERY_ACK_LATE = True

CELERYD_MAX_TASKS_PER_CHILD = 100

CLELERYD_TASK_TIME_LIMIT = 12 * 30


#run task at setup,and clear pending status
from celery.signals import celeryd_init
@celeryd_init.connect(sender=None)
def run_at_celery_setup(conf=None, **kwargs):
    print("#########hahaha##############")
    #clear pending task at setup
    from MAIN.tasks.ClearPending import ClearPendingTask
    print("Run ClearPendingTask !")
    ClearPendingTask.delay()