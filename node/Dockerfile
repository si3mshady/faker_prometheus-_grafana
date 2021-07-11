FROM node:slim

WORKDIR  /app

ADD ./app.js .

ADD package.json .

RUN npm i package.json 

EXPOSE 888

ENTRYPOINT [ "node" ]

CMD [ "app.js" ]

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -X POST -f '{}'  http://localhost:888/data || exit 1

