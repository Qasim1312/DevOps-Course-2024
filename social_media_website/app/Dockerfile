# Use a lightweight Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install system dependencies required by Pillow
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && apt-get clean

# Copy the requirements file into the image
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the image
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
