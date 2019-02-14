FROM python:3.6.8-slim 
FROM node:10-slim

RUN mkdir /app
WORKDIR /app

RUN npm i -g newman
RUN npm i -g newman-reporter-html

ADD requeriments.txt /app
RUN pip install -r requeriments.txt 

expose 8000