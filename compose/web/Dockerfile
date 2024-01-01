FROM node:18-alpine
WORKDIR /usr/src/app
COPY ./dashboard/package*.json ./
RUN npm install
COPY ./dashboard ./

CMD [ "npm", "run", "dev"]
