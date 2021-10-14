FROM python:3.9

COPY . /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt
