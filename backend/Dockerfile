FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY . /app/backend

WORKDIR /app/backend

RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=2000", "--reload" ]
