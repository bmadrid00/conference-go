#base image for python 3 latest version
FROM python:3

#names working directory in docker container /app
WORKDIR /app

#copy all these files into /app in docker container
COPY accounts accounts
COPY attendees attendees
COPY common common
COPY conference_go conference_go
COPY events events
COPY presentations presentations
COPY requirements.txt requirements.txt
COPY manage.py manage.py

#download all requirements
RUN pip install -r requirements.txt

#run with gunicorn as it is faster --- used for deployment
CMD gunicorn --bind 0.0.0.0:8000 conference_go.wsgi
