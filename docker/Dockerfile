FROM python:3.8.9

RUN mkdir /django_app
WORKDIR /django_app
ADD . /django_app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED ""

ENV DJANGO_SUPERUSER_USERNAME "username"
ENV DJANGO_SUPERUSER_PASSWORD "password"
ENV DJANGO_SUPERUSER_EMAIL "email@gmail.com"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN rm -rf db.sqlite3
RUN rm -rf gpt2/migrations
RUN python manage.py makemigrations gpt2
RUN python manage.py migrate

RUN python manage.py createsuperuser --noinput
EXPOSE 8000

CMD ["python", "/django_app/manage.py", "runserver", "0.0.0.0:8000"]
