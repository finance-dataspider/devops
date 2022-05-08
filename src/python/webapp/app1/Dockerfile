FROM python:3.8-slim-buster
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app_1.py .
ENTRYPOINT ["python","/app_1.py"]