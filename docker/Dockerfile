
FROM python:3.7

RUN apt-get update && apt-get upgrade -y

EXPOSE 8080

WORKDIR /src

COPY ./requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt
