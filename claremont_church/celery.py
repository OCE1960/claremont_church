import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'claremont_church.settings')

app = Celery('claremont_church',
             broker='amqp://',
             backend='rpc://',
             )

class Config:
    enable_utc = True
    timezone = 'Europe/London'

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object(f'claremont_church.settings', namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.config_from_object(Config)

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
    
if __name__ == '__main__':
    app.start()
