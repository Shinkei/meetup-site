FROM python:3.6-alpine3.8

RUN apk update && apk --no-cache add \
    postgresql-dev=10.5-r0 \
    gcc=6.4.0-r8 \
    musl-dev=1.1.19-r10 \
    g++=6.4.0-r8 \
    make=4.2.1-r2 \
    linux-headers=4.4.6-r2

RUN cd /tmp && mkdir gdal && \
    wget https://download.osgeo.org/gdal/2.3.1/gdal-2.3.1.tar.gz -O gdal.tar.gz && \
    tar xzf gdal.tar.gz -C gdal --strip-components 1 && cd gdal && \
    ./configure && make && make install && \
    cd /tmp && rm -r gdal

RUN addgroup -g 1000 python && adduser -u 1000 -G python -s /bin/sh -D python

USER python

ENV PATH "/home/python/.local/bin:$PATH"
WORKDIR /tmp
ADD requirements.txt /tmp/
RUN pip install --user -r /tmp/requirements.txt

WORKDIR /home/python/app

ENV FLASK_RUN_PORT 8080
EXPOSE 8080

ADD init.sh /
ADD wsgi.sh /

CMD ["flask", "run", "--host=0.0.0.0"]
