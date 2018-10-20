FROM resin/raspberrypi3-debian:stretch

ENV INITSYSTEM on

RUN  apt-get update && apt-get install -yq \
    git \
    python3 \
    python3-dev \
    python3-pip \
    build-essential \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /cloud_connector
COPY requirements.txt .
RUN pip3 install -r /requirements.txt
COPY . /cloud_connector

WORKDIR /cloud_connector

CMD ["python3", "runner.py"]