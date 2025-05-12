FROM python:3.11-slim

# Create a folder /app if it doesn't exist,
# the /app folder is the current working directory
WORKDIR /app

COPY ./main.py /app

COPY ./requirements.txt /app

COPY ./model /app/model

EXPOSE 30000

RUN pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "30000"]