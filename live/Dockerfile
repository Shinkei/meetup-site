FROM nginx:1.15-alpine

RUN apk update && apk --no-cache add \
    bats=0.4.0-r2 \
    curl=7.61.0-r0 \
    make=4.2.1-r0 \
    wget=1.19.5-r0 \
    perl=5.26.2-r1 \
    perl-io-socket-ssl=2.048-r1 \
    openssl=1.0.2o-r1 \
    certbot=0.19.0-r0 \
    py2-pip=9.0.1-r1 \
    busybox-suid=1.27.2-r11

RUN pip install certbot-nginx==0.26.1

RUN deluser nginx && adduser -h /home/nginx -D nginx

RUN cd /tmp && mkdir ddclient && \
    wget https://cpanmin.us/ -O /usr/local/bin/cpanm && \
    chmod +x /usr/local/bin/cpanm && \
    cpanm Data::Validate::IP && \
    wget https://github.com/ddclient/ddclient/tarball/v3.9.0 -O ddclient.tar.gz && \
    tar xzf ddclient.tar.gz -C ddclient --strip-components=1 && cd ddclient && \
    mv ddclient /usr/sbin/ && mkdir /etc/ddclient && mkdir /var/cache/ddclient && \
    cd /tmp && rm -r ddclient

RUN touch /var/run/nginx.pid && \
    chown -R nginx /var/run/nginx.pid && \
    chown -R nginx /var/cache/nginx && \
    chown -R nginx /etc/nginx

RUN touch /var/run/ddclient.pid && \
    chown -R nginx /var/run/ddclient.pid && \
    chown -R nginx /var/cache/ddclient && \
    touch /etc/ddclient/ddclient.conf && \
    chown nginx /etc/ddclient/ddclient.conf && \
    chmod 600 /etc/ddclient/ddclient.conf

RUN mkdir /var/lib/letsencrypt && \
    chown -R nginx /var/lib/letsencrypt && \
    mkdir /var/log/letsencrypt && \
    chown -R nginx /var/log/letsencrypt && \
    mkdir /etc/letsencrypt && \
    chown -R nginx /etc/letsencrypt

ADD etc/ddclient/conf.template /etc/ddclient/


WORKDIR /home/nginx

ADD init.sh /

USER nginx

ENTRYPOINT ["/init.sh"]

CMD ["nginx", "-g", "daemon off;"]
