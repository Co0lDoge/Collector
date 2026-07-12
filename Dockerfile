FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

# Install core dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy core framework only
COPY core/ ./core/
COPY main.py app.py settings.py entrypoint.sh ./
RUN chmod +x entrypoint.sh

# Create plugin folders
RUN mkdir -p /app/providers /app/storages

# Use ENTRYPOINT to point to the shell script
ENTRYPOINT ["/app/entrypoint.sh"]