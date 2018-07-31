FROM nginx:1.15-alpine

RUN touch /var/run/nginx.pid && \
    chown -R nginx /var/run/nginx.pid && \
    chown -R nginx /var/cache/nginx

USER nginx
