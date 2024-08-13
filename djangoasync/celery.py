from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

app = Celery('myproject')

app.config_from_object('tasks', broker='pyamqp://guest@localhost//')
app.autodiscover_tasks()