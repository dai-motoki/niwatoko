FROM python:3.11

RUN apt -y update && apt -y upgrade
RUN apt -y install libopencv-dev

RUN pip install niwatoko litellm

WORKDIR /app