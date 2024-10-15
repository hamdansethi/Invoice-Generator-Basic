# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    libcairo2 \
    libpango1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install WeasyPrint
RUN pip install WeasyPrint

# Command to run your application (adjust as needed)
CMD ["python", "app.py"]
