from __future__ import absolute_import,unicode_literals

import os
from celery import Celery

from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery.settings')


app= Celery('django_celery')

app.conf.enable_utc=False

app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings,namespace='CELERY')

#celery beat settings
#celery beat is used to schedule task to schelery worker
app.conf.beat_schedule = {
   'send-mail-every-day-at-8':{
       'task':'send_mail_app.tasks.send_mail_func',
       'schedule':crontab(hour=17,minute=1)
   } 
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")