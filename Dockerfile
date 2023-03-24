FROM python:3


ENV PYHTONUNBUFFERED 1


WORKDIR /app


COPY . .


RUN pip install -r requirements.txt


CMD python manage.py runserver '0.0.0.0:8000'
