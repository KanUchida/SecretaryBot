BROKER_URL = 'redis://127.0.0.1:6379',
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_IMPORTS = ('tasks.sample', )
CELERY_TASK_RESULT_EXPIRES = 18000  # 5 hours.

