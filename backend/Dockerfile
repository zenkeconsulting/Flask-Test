FROM python:slim-buster as build

COPY . /srv/flask_app/backend

WORKDIR /srv/flask_app/backend

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && apt-get -y install wkhtmltopdf

FROM build AS development

# for dev environment
RUN apt-get -y install git

RUN pip install -r requirements.txt --src /usr/local/src

COPY nginx.conf /etc/nginx

RUN chown -R www-data:www-data ./templates

RUN chmod +x ./start.sh

EXPOSE 80

CMD ["./start.sh"]
