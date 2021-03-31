import os
from celery import Celery
from celery.schedules import crontab
from celery.schedules import solar

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'news.tasks.every_week_mailing',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

