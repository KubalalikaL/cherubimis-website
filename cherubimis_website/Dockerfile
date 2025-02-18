
# cherubimis_website/Dockerfile

FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["/bin/sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn cybersec_project.wsgi:application --bind 0.0.0.0:8000"]
