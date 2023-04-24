from celery.schedules import crontab
from celery import Celery
from django.conf import settings
import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_celery_app.settings')

app=Celery("dj_celery_app")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'every_10_miutes':{
        'task' : 'scrape_hacker_news_rss_feed',
        'schedule' : crontab()
    }
}

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


