FROM python:3.8-slim-buster
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY home.py .
ENTRYPOINT ["python","/home.py"]