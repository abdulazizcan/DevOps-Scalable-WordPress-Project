FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt

COPY container_monitor.py .  

CMD ["python3", "/app/container_monitor.py"]  
