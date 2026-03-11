# Start from a small Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and buffer issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Copy dependency list first (better Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Flask runs on port 5000 by default
EXPOSE 5000

# Command to run the application
CMD ["python", "SiteSide.py"]