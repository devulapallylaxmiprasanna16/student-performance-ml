FROM python:3.10-slim

WORKDIR /app

# Ensure python command exists
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

EXPOSE 8000

# Run with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
