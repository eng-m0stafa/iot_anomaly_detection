FROM python:3.8-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only the necessary files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the Python files and configuration files
COPY app.py .
COPY models.py .
COPY train_models.py .
COPY prometheus.yml .
COPY dashboard.json .

# Create necessary directories
RUN mkdir -p Master CyPhy models

# Copy model files
COPY models/*.pth models/

# Expose the API port
EXPOSE 8005

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "app.py"] 