FROM FROM resin/raspberrypi3-debian:stretch

ENV INITSYSTEM on

RUN apk add --update \
    git \
    python-dev \
    build-base \
  && rm -rf /var/cache/apk/*

RUN mkdir /cloud_connector
COPY requirements.txt .
RUN pip install -r /requirements.txt
COPY . /cloud_connector

WORKDIR /cloud_connector

CMD ["python", "runner.py"]