FROM python:3.7-slim
COPY . /worker_app/
WORKDIR /worker_app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A workers worker