FROM python:3.11-slim

LABEL maintainer="ducptit"
LABEL organization="Mlops"

WORKDIR /mlflow/

ARG MLFLOW_VERSION

RUN apt-get update -y
RUN apt-get install -y iputils-ping
RUN pip install --no-cache-dir mlflow==${MLFLOW_VERSION} psycopg2-binary
 
# docmentation purpose only
EXPOSE 5000

CMD mlflow server \ 
--backend-store-uri ${BACKEND_STORE_URI} \
--sever-artifacts \
--host 0.0.0.0 \
--port 5000 
# --port 5000: cổng port mà mlflow sẽ chạy trên container


# 1. docker build -t before_msb -f mlflow/Dockerfile --build-arg MLFLOW_VERSION=2.3.2 mlflow
# -f mlflow/Dockerfile: Chỉ định Dockerfile không nằm ở thư mục hiện tại mà là mlflow/Dockerfile
# mlflow: Là build context, tức là toàn bộ thư mục mlflow/ sẽ được Docker gửi vào quá trình build (bao gồm Dockerfile và các file khác)

# 2. docker run before_msb
# 3. docker exec -ti before_msb bash

