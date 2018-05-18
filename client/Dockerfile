FROM node:alpine

USER node

WORKDIR /tmp
ENV PATH "/tmp/node_modules/.bin:$PATH"
ADD package.json yarn.lock /tmp/
RUN yarn

WORKDIR /home/node/app

EXPOSE 3000

ADD init.sh /
ENTRYPOINT ["/init.sh"]

CMD ["yarn", "start"]
