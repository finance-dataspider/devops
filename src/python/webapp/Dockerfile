FROM python:3.7-slim AS compile-image
RUN mkdir /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py /app/.
COPY version /
CMD ["python", "/app/app.py"]