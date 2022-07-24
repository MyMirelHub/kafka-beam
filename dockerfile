FROM openjdk:11

RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip \
    python3-wheel

WORKDIR /app

COPY requirements.txt requirements.txt
COPY producer2.py producer2.py

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "producer2.py", "--sdk_harness_container_image_overrides", ".*java.*,chamikaramj/beam_java11_sdk:latest","--environment_type=DOCKER" ]