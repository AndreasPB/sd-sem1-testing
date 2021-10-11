FROM python:3.9

COPY . .

WORKDIR /app

RUN pip3 install -r requirements.txt
