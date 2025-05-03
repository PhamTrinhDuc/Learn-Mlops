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

### Ví dụ cụ thể về Dockerfile:
Dưới đây là một Dockerfile cho ứng dụng Node.js đơn giản:

```Dockerfile
# Sử dụng image Node.js phiên bản 18, biến thể alpine để nhẹ
FROM node:18-alpine

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép package.json và package-lock.json
COPY package*.json ./

# Cài đặt phụ thuộc
RUN npm install

# Sao chép toàn bộ mã nguồn
COPY . .

# Thiết lập biến môi trường
ENV PORT=3000

# Mở cổng
EXPOSE 3000

# Lệnh khởi động ứng dụng
CMD ["npm", "start"]
```

- **Giải thích**:
  - `FROM node:18-alpine`: Dùng image Node.js nhẹ.
  - `WORKDIR /app`: Đặt thư mục làm việc là `/app`.
  - `COPY package*.json ./`: Sao chép tệp cấu hình npm trước để tối ưu hóa bộ nhớ cache.
  - `RUN npm install`: Cài đặt phụ thuộc.
  - `COPY . .`: Sao chép mã nguồn.
  - `ENV PORT=3000`: Đặt cổng mặc định.
  - `EXPOSE 3000`: Thông báo container lắng nghe cổng 3000.
  - `CMD ["npm", "start"]`: Chạy lệnh `npm start` khi container khởi động.

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