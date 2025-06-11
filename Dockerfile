# Use a minimal base image with Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Expose port for the container
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]