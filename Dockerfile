FROM mikeallanson/python3-node:0.0.8

RUN mkdir /app
WORKDIR /app

RUN npm i -g newman
RUN npm i -g newman-reporter-html

ADD requeriments.txt /app
RUN pip install -r requeriments.txt 

expose 8000