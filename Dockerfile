FROM python:3.11-slim

RUN apt-get update &&\
    apt-get upgrade -y

WORKDIR /app

COPY requirements.txt requirements.txt

COPY ./src /app

RUN pip install --upgrade pip &&\
    pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["python", "-m", "main"]
