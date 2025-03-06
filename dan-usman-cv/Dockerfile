FROM python:3.9-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app.py .
COPY static/ static/

# Create static directory if it doesn't exist and move HTML file there
RUN mkdir -p static
COPY templates/index.html static/index.html

# Expose port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]