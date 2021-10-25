FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

COPY . /app

WORKDIR /app/app

RUN pip install --no-cache-dir -r ../requirements.txt

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--port=2000", "--reload" ]
