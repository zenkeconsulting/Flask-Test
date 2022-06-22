FROM python:3.8-slim-buster

RUN apt-get update && apt-get install -y \
  wkhtmltopdf \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]