<!-- install docker: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04 -->

# Dockerfile, Docker Image và Container

## Định nghĩa:
- **Dockerfile**: Là một tệp văn bản chứa các lệnh để xây dựng một Docker image. Nó mô tả cách tạo image, bao gồm hệ điều hành cơ bản, cài đặt phần mềm, cấu hình môi trường, và các lệnh để chạy ứng dụng.
- **Docker Image**: Là một bản mẫu chỉ đọc (read-only) được tạo từ Dockerfile, chứa tất cả các thành phần cần thiết để chạy một ứng dụng (mã nguồn, thư viện, công cụ, cấu hình).
- **Docker Container**: Là một thể hiện (instance) của Docker image, chạy như một quá trình độc lập trên máy chủ, cung cấp môi trường cô lập để thực thi ứng dụng.

## Cấu trúc cơ bản của tệp Dockerfile:
Tệp Dockerfile bao gồm các lệnh theo thứ tự thực thi để xây dựng image. Cú pháp cơ bản bao gồm các chỉ thị (instruction) như sau:

```Dockerfile
# Chỉ định image cơ sở
FROM <image>:<tag>

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép tệp vào image
COPY <source> <destination>

# Cài đặt các phụ thuộc hoặc chạy lệnh
RUN <command>

# Thiết lập biến môi trường
ENV <key>=<value>

# Mở cổng mà container sẽ lắng nghe
EXPOSE <port>

# Lệnh mặc định khi container khởi động
CMD ["executable", "param1", "param2"]
```

### Các chỉ thị chính trong Dockerfile:
#### 1. **FROM**:
- Chỉ định image cơ sở để bắt đầu xây dựng.
- Ví dụ:
  ```Dockerfile
  FROM node:18-alpine
  ```
  - Sử dụng image `node` phiên bản `18` với biến thể `alpine` (nhẹ).

#### 2. **WORKDIR**:
- Thiết lập thư mục làm việc mặc định cho các lệnh tiếp theo.
- Ví dụ:
  ```Dockerfile
  WORKDIR /usr/src/app
  ```
  - Các lệnh `COPY`, `RUN`, `CMD` sẽ hoạt động trong thư mục `/usr/src/app`.

#### 3. **COPY** và **ADD**:
- Sao chép tệp/thư mục từ máy host vào image.
- `COPY` thường được sử dụng hơn vì đơn giản hơn.
- Ví dụ:
  ```Dockerfile
  COPY package.json /app/
  COPY src/ /app/src/
  ```
  - Sao chép `package.json` và thư mục `src` vào `/app`.

#### 4. **RUN**:
- Thực thi lệnh trong quá trình xây dựng image (ví dụ: cài đặt gói, cập nhật hệ thống).
- Ví dụ:
  ```Dockerfile
  RUN npm install
  RUN apt-get update && apt-get install -y python3
  ```
  - Cài đặt các phụ thuộc Node.js và Python 3.

#### 5. **ENV**:
- Thiết lập biến môi trường trong image.
- Ví dụ:
  ```Dockerfile
  ENV NODE_ENV=production
  ENV PORT=3000
  ```

#### 6. **EXPOSE**:
- Chỉ định cổng mà container sẽ lắng nghe (không tự động ánh xạ cổng).
- Ví dụ:
  ```Dockerfile
  EXPOSE 8080
  ```

#### 7. **CMD**:
- Xác định lệnh mặc định khi container khởi động.
- Chỉ có một `CMD` được thực thi; nếu có nhiều, chỉ lệnh cuối cùng có hiệu lực.
- Có thể ghi đè khi chạy container với `docker run`.
- Ví dụ:
  ```Dockerfile
  CMD ["npm", "start"]
  CMD ["python3", "app.py"]
  ```

#### 8. **ENTRYPOINT**:
- Chỉ định lệnh chính không thể ghi đè dễ dàng (thường dùng cho các container chạy script cụ thể).
- Ví dụ:
  ```Dockerfile
  ENTRYPOINT ["python3", "app.py"]
  ```

#### 9. **VOLUME**:
- Chỉ định thư mục trong container để lưu trữ dữ liệu bền vững hoặc chia sẻ với host.
- Ví dụ:
  ```Dockerfile
  VOLUME /app/data
  ```

#### 10. **USER**:
- Chỉ định người dùng chạy container (mặc định là `root`).
- Ví dụ:
  ```Dockerfile
  USER node
  ```

## Ví dụ cụ thể về Dockerfile:
Dưới đây là một Dockerfile cho ứng dụng mflow đơn giản:

```Dockerfile
FROM python:3.11-slim

LABEL maintainer="ducptit"
LABEL organization="Mlops"

WORKDIR /mlflow/

ARG MLFLOW_VERSION

RUN apt-get update -y
RUN apt-get install -y iputils-ping
RUN pip install --no-cache-dir mlflow==${MLFLOW_VERSION}

# documentation purpose only
EXPOSE 5000

CMD mlflow server \
  --backend-store-uri ${BACKEND_STORE_URI} \
  --serve-artifacts \
  --host 0.0.0.0 \
  --port 5000
```

- **Giải thích**:
  | Tham số | Ý nghĩa | Cách hoạt động |
|---------|---------|----------------|
| `FROM python:3.11-slim` | Chỉ định image cơ sở là Python 3.11 phiên bản nhẹ (slim). | Docker tải image `python:3.11-slim` từ Docker Hub làm nền tảng, các lệnh tiếp theo xây dựng trên image này. |
| `LABEL maintainer="ducptit"` | Thêm siêu dữ liệu chỉ định người duy trì image là "ducptit". | Lưu nhãn `maintainer` vào siêu dữ liệu image, có thể xem bằng `docker inspect`. |
| `LABEL organization="Mlops"` | Thêm siêu dữ liệu chỉ định tổ chức là "Mlops". | Lưu nhãn `organization` vào siêu dữ liệu image, hỗ trợ quản lý và tra cứu. |
| `WORKDIR /mlflow/` | Thiết lập thư mục làm việc mặc định là `/mlflow/`. | Đặt ngữ cảnh cho các lệnh tiếp theo trong thư mục `/mlflow/`, tạo thư mục nếu chưa tồn tại. |
| `ARG MLFLOW_VERSION` | Khai báo biến build-time `MLFLOW_VERSION`. | Lưu biến để sử dụng trong build, giá trị được truyền qua `--build-arg` khi chạy `docker build`. |
| `RUN apt-get update -y` | Cập nhật danh sách gói phần mềm từ repository. | Chạy lệnh trong container tạm thời, lưu danh sách gói cập nhật vào một lớp mới của image. |
| `RUN apt-get install -y iputils-ping` | Cài đặt công cụ `ping` để kiểm tra kết nối mạng. | Chạy lệnh cài đặt `iputils-ping`, lưu kết quả vào một lớp mới, công cụ có sẵn khi chạy container. |
| `RUN pip install --no-cache-dir mlflow==${MLFLOW_VERSION}` | Cài đặt thư viện MLflow với phiên bản được chỉ định. | Chạy lệnh cài đặt MLflow, không lưu cache pip, lưu thư viện vào một lớp mới của image. |
| `EXPOSE 5000` | Thông báo container lắng nghe cổng 5000. | Ghi chú cổng 5000 vào siêu dữ liệu image, không thực sự mở cổng, cần ánh xạ khi chạy container. |
| `CMD mlflow server ...` | Chỉ định lệnh chạy server MLflow khi container khởi động. | Lưu lệnh khởi động server MLflow với các tham số (`--backend-store-uri`, `--serve-artifacts`, `--host 0.0.0.0`, `--port 5000`) để thực thi khi container chạy. |

## Quá trình từ Dockerfile đến Container:
1. **Xây dựng Image**:
   - Sử dụng lệnh:
     ```bash
     docker build -t <image_name>:<tag> .
     ```
     - `-t`: Đặt tên và tag cho image.
     - `.`: Đường dẫn đến thư mục chứa Dockerfile (thư mục hiện tại).
   - Ví dụ:
     ```bash
     docker build -t myapp:1.0 .
     ```

2. **Kiểm tra Image**:
   - Xem danh sách image:
     ```bash
     docker images
     ```

3. **Chạy Container từ Image**:
   - Sử dụng lệnh:
     ```bash
     docker run -d -p <host_port>:<container_port> --name <container_name> <image_name>:<tag>
     ```
     - `-d`: Chạy ở chế độ nền.
     - `-p`: Ánh xạ cổng.
     - `--name`: Đặt tên container.
   - Ví dụ:
     ```bash
     docker run -d -p 3000:3000 --name myapp_container myapp:1.0
     ```

4. **Kiểm tra Container**:
   - Xem danh sách container đang chạy:
     ```bash
     docker ps
     ```
   - Xem tất cả container (bao gồm đã dừng):
     ```bash
     docker ps -a
     ```

5. **Quản lý Container**:
   - Dừng container:
     ```bash
     docker stop <container_name>
     ```
   - Khởi động lại:
     ```bash
     docker restart <container_name>
     ```
   - Xóa container:
     ```bash
     docker rm <container_name>
     ```
   - Xóa image:
     ```bash
     docker rmi <image_name>:<tag>
     ```

6. **Xem log của Container**:
   - Xem log để debug:
     ```bash
     docker logs <container_name>
     ```

## Các lệnh tương tác với Docker Image và Container:
#### 1. Xây dựng image:
```bash
docker build -t myapp:1.0 .
```

#### 2. Chạy container:
```bash
docker run -d -p 3000:3000 --name myapp_container myapp:1.0
```

#### 3. Kiểm tra trạng thái:
```bash
docker ps
```

#### 4. Xem log:
```bash
docker logs myapp_container
```

#### 5. Dừng và xóa container:
```bash
docker stop myapp_container
docker rm myapp_container
```

#### 6. Xóa image:
```bash
docker rmi myapp:1.0
```

#### 7. Đẩy image lên Docker Hub:
- Đăng nhập:
  ```bash
  docker login
  ```
- Đặt tag cho image:
  ```bash
  docker tag myapp:1.0 username/myapp:1.0
  ```
- Đẩy image:
  ```bash
  docker push username/myapp:1.0
  ```

#### 8. Kéo image từ Docker Hub:
```bash
docker pull username/myapp:1.0
```

## Lưu ý khi sử dụng Dockerfile:
- **Tối ưu hóa Image**:
  - Sử dụng image cơ sở nhẹ (như `alpine`).
  - Gộp các lệnh `RUN` để giảm số layer (ví dụ: `RUN apt-get update && apt-get install -y ...`).
  - Xóa các tệp tạm không cần thiết trong cùng lệnh `RUN`.
- **Bộ nhớ cache**:
  - Docker lưu trữ cache cho các bước trong Dockerfile. Thay đổi tệp hoặc lệnh sẽ làm mất cache từ bước đó trở đi.
  - Đặt các lệnh ít thay đổi (như `COPY package.json` và `RUN npm install`) trước các lệnh thay đổi thường xuyên (như `COPY src/`).
- **Bảo mật**:
  - Tránh sử dụng user `root` trong container (`USER`).
  - Không để lộ thông tin nhạy cảm (mật khẩu, API key) trong Dockerfile.
- **Đa nền tảng**:
  - Nếu cần hỗ trợ nhiều kiến trúc (x86, ARM), sử dụng `buildx`:
    ```bash
    docker buildx build --platform linux/amd64,linux/arm64 -t myapp:1.0 .
    ```