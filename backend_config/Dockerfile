FROM python:3.11.7-alpine

WORKDIR /dd_back

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ../backend_config .
COPY ../api_v1 .
COPY ../media .
COPY ../nginx .
COPY ../.env .
COPY ../digdispdata.json .
COPY ../manage.py .
COPY ../requirements.txt .