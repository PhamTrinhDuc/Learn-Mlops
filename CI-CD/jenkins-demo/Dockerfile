FROM python:3.9-slim
WORKDIR /app
COPY app/ ./app
COPY tests/ ./tests
COPY app/requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "app/main.py"]
