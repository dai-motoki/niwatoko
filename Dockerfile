FROM python:3.11

RUN pip install niwatoko litellm

WORKDIR /app