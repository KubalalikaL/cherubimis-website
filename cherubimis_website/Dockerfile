# ============ STAGE 1: BUILD ENVIRONMENT =============
FROM python:3.11-slim as builder
LABEL maintainer="lkubalalika"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      gcc \
      python3-dev \
      default-libmysqlclient-dev \
      build-essential \
      libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /website

COPY requirements.txt /website/

# Install dependencies
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . /website
RUN chmod +x scripts/run.sh 
RUN python manage.py collectstatic --noinput

# ============ STAGE 2: FINAL, RUNTIME IMAGE =============
FROM python:3.11-slim as runtime

RUN useradd --system --home /website --uid 1001 appuser

WORKDIR /website

# Copy installed Python packages and Gunicorn from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# Copy project code
COPY --from=builder /website /website

USER appuser
EXPOSE 8000

ENTRYPOINT ["./scripts/run.sh"]
