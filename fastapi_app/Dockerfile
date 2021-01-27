FROM tiangolo/uvicorn-gunicorn-fastapi
COPY . /fastapi_app/
WORKDIR /fastapi_app/
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT uvicorn main_app:app --host=0.0.0.0 --port=8080