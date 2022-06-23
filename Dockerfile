FROM python:3.6.8-alpine3.9

WORKDIR /var/www/

ADD . /var/www/
RUN apk add --no-cache build-base libffi-dev openssl-dev ncurses-dev

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt // gunicorn is install inside requirements.txt

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]