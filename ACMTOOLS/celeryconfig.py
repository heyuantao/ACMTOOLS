import djcelery

djcelery.setup_loader()



CELERY_IMPORTS = (
    'MAIN.tasks.AntiCheating',
    'MAIN.tasks.CodeExport',
    'MAIN.tasks.ClearPending'
)

CELERYD_FORCE_EXECV =True

CELERYD_CONCURRENCY = 1

CELERY_ACK_LATE = True

CELERYD_MAX_TASKS_PER_CHILD = 100

CLELERYD_TASK_TIME_LIMIT = 12 * 30
