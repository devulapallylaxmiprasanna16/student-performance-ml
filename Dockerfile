FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (Render uses 8000)
EXPOSE 8000

# Start app with gunicorn (NO python command)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
