import time
from celery import Celery

app = Celery('consumer',
            broker='amqp://myadmin:password@rabbit:5672',
            backend='redis://redis-service:6379/0')

@app.task
def add_fn(num1,num2):
    time.sleep(int(num1)+int(num2))
    return num1+num2