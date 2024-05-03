import structlog
from celery.utils.log import get_task_logger

from bittensor_panel.celery import app

logger = structlog.wrap_logger(get_task_logger(__name__))


@app.task
def demo_task(x, y):
    logger.info("adding two numbers", x=x, y=y)
    return x + y
