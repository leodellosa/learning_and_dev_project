# Use official Python base image
FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Move to the folder where Tailwind's package.json is
WORKDIR /app/learning_and_development/theme/static_src

# Install Tailwind dependencies
RUN npm install

# Set dummy env var so Django doesn't crash at build time
# ENV SECRET_KEY=dummy-build-secret

WORKDIR /app/learning_and_development
RUN python manage.py tailwind install
RUN python manage.py tailwind build

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput


# Expose the application port
EXPOSE 8087

# Start Django
CMD ["gunicorn", "learning_and_development.wsgi:application", "--bind", "0.0.0.0:8087", "--timeout", "90"]
