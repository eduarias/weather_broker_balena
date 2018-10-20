FROM resin/raspberrypi3-debian:stretch

ENV INITSYSTEM on

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
COPY . /usr/src/app
WORKDIR /usr/src/app

# Finally, start our app
CMD ["python3", "/usr/src/app/app.py"]