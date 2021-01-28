from fastapi import FastAPI, status
from loguru import logger
from celery import Celery

app = FastAPI()
api_task_queue = Celery('producer',
                broker='amqp://myadmin:password@rabbit:5672',
                backend='redis://redis-service:6379/0')



@app.get('/health', status_code=status.HTTP_200_OK)
def root():
    logger.info('Pinging health check')
    return {'OK'}

@app.post('/add/{num1}/{num2}', status_code=status.HTTP_202_ACCEPTED)
def add_fn(num1: float,num2: float):
    r = api_task_queue.send_task('workers.add_fn', kwargs={'num1': num1, 'num2': num2})
    return r.id

@app.get('/get_task_status/{task_id}', status_code=status.HTTP_200_OK)
def get_task_status(task_id):
    status = api_task_queue.AsyncResult(task_id)
    return {'Status of the job {}: {}'.format(task_id, str(status.state))}

@app.get('/get_task_result/{task_id}', status_code=status.HTTP_200_OK)
def get_task_result(task_id):
    status = api_task_queue.AsyncResult(task_id)
    if status.state != 'SUCCESS':
        return {'Status of the job {}: {}'.format(task_id, str(status.state))}
    else:
        return {'Result of the job {}: {}'.format(task_id, str(status.result))}