FROM resin/raspberrypi3-debian:stretch

RUN apt-get update && apt-get install -yq \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-sense-hat \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip3 install -r /requirements.txt
RUN mkdir /app
COPY . /app

WORKDIR /app

CMD ["python3", "app.py"]