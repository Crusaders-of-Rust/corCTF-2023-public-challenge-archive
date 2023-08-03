# Stage 1: Build Python environment
FROM python:3.9.2 AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY Pipfile Pipfile.lock /app/

RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --system --deploy

COPY . /app/

# Stage 2: Run Django app with Gunicorn and Nginx
FROM python:3.9.2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    nginx \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Copy the Python environment from the previous stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Install Gunicorn in the second stage
RUN pip install gunicorn


# Copy Nginx configuration
COPY deployment/nginx.conf /etc/nginx/sites-available/default

# Copy Supervisor configuration
COPY deployment/supervisor.conf /etc/supervisor/conf.d/

# Copy Django project files
COPY . /app/

RUN mv /app/flag.txt /flag.txt

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 80

# Start Supervisor to manage Gunicorn and Nginx processes
CMD ["supervisord", "-n"]
