from __future__  import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab, schedule
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CryptoPrice.settings')
app=Celery('CryptoPrice')
app.conf.enable_utc=True
app.config_from_object(settings,namespace='CELERY')

app.conf.beat_schedule={
    'every-10-second':{
        'task':'bitcoin.tasks.update_price_hour',
        'schedule': crontab(minute='*/2'),
    },
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')

#celery worker
# celery -A CryptoPrice.celery worker --pool=solo -l info
#celery beat
#celery -A CryptoPrice beat -l INFO
