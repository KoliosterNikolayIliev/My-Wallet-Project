FROM python:3.9-alpine
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
