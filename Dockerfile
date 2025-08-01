FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY django_project/. .

ENV PYTHONUNBUFFERED=1 DJANGO_SETTINGS_MODULE=myproject.settings

EXPOSE 8000

CMD gunicorn --workers 3 --bind 0.0.0.0:8000 myproject.wsgi:application