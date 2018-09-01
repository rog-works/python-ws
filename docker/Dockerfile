FROM python:3.6-alpine

RUN pip install pyyaml \
 && ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
 && echo "Asia/Tokyo" > /etc/timezone

WORKDIR /opt/app
