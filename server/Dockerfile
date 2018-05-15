FROM python:alpine

RUN addgroup -g 1000 python && adduser -u 1000 -G python -s /bin/sh -D python

USER python

ENV PATH "/home/python/.local/bin:$PATH"
WORKDIR /tmp
ADD requirements.txt /tmp/
RUN pip install --user -r /tmp/requirements.txt

WORKDIR /home/python/app

ENV FLASK_RUN_PORT 8080
EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0"]