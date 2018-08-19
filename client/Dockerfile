FROM node:8.11-alpine

WORKDIR /tmp
ENV PATH "/tmp/node_modules/.bin:$PATH"
ADD package.json yarn.lock /tmp/
RUN yarn

WORKDIR /home/node/app

EXPOSE 3000

USER node

ADD init.sh /
ENTRYPOINT ["/init.sh"]

CMD ["yarn", "start"]
