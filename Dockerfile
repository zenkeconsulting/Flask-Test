FROM python:slim-buster

COPY . /srv/flask_app

WORKDIR /srv/flask_app

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && apt-get -y install wkhtmltopdf

RUN pip install -r requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx

RUN chown -R www-data:www-data ./templates

RUN chmod +x ./start.sh

CMD ["./start.sh"]
