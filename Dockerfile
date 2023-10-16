FROM python:3.11-slim

RUN apt-get update &&\
    apt-get upgrade -y

WORKDIR /app

COPY ./src /app

RUN pip install --upgrade pip &&\
    pip install -r requirements.txt --no-cache-dir

CMD ["python", "main.py"]
