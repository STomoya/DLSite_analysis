
FROM python:3.7

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    make

EXPOSE 8080

WORKDIR /src

COPY ./requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt
