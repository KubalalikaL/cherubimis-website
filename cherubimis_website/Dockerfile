# ============ STAGE 1: BUILD ENVIRONMENT =============
FROM python:3.11-slim as builder
LABEL maintainer="lkubalalika"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install && apt-get install gcc python3-dev default-libmysqlclient-dev -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /website

COPY requirements.txt /website/

# Install dependencies
RUN pip install -U pip setuptools wheel && pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /website
RUN chmod +x scripts/run.sh 
RUN python manage.py collectstatic --noinput

# ============ STAGE 2: FINAL, RUNTIME IMAGE =============
FROM python:3.11-slim as runtime

# Create an unprivileged user and group
RUN useradd --system --home /website --uid 1001 appuser

# Set working directory
WORKDIR /website

# Copy installed Python packages from "builder" stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

COPY --from=builder /website /website
USER appuser
EXPOSE 8000

# Add entrypoint script
ENTRYPOINT ["./scripts/run.sh"]
