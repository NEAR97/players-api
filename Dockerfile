FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /players
WORKDIR /players
COPY requirements.txt /players/
RUN pip install -r requirements.txt
COPY . /players/
CMD python manage.py runserver --settings=settings.production 0.0.0.0:8080