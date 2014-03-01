from __future__ import absolute_import
from django.conf import settings
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

from celery import Celery

app = Celery('biostar')

# Read the configuration from the config file.
app.config_from_object(settings.CELERY_CONFIG)

# Discover tasks in applications.
app.autodiscover_tasks(
    lambda: ["biostar.mailer"]
)

@app.task
def test(*args, **kwds):
    logger.info("*** executing task %s %s, %s" % (__name__, args, kwds))
    return 1000



