FROM python:3.7-slim AS compile-image
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
CMD ["python", "/app.py"]