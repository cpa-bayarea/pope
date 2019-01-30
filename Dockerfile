FROM python:3.6-alpine

RUN apk update && apk --no-cache add \
    tzdata \
    py3-pillow \
    zlib \
    zlib-dev \
    jpeg-dev \
    build-base \
    python3-dev 

WORKDIR /root/pope
COPY . .
RUN ./setup.py install && mdkir -p /root/pope/data

EXPOSE 8000
CMD ["gunicorn", "pope.wsgi:application", "-w", "10", "-b", "0.0.0.0:8000"]
