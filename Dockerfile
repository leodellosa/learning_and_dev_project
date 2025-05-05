# Use official Python base image
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
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
COPY learning_and_development/ .

# Tailwind setup in theme app
WORKDIR /app/theme

# Install Tailwind dependencies
RUN npm install

# Run tailwind install via django-tailwind (sets up static_src, config files)
RUN python ../manage.py tailwind install

# Build Tailwind CSS
RUN python ../manage.py tailwind build

# --- Static files collection ---
WORKDIR /app
RUN python manage.py collectstatic --noinput


# Start Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
