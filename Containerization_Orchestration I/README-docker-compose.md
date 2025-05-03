
## Định nghĩa:
Docker Compose là một công cụ để định nghĩa và chạy các ứng dụng Docker đa container bằng cách sử dụng tệp cấu hình YAML. Tệp docker-compose.yml được sử dụng để mô tả các service, network, volume và các cấu hình khác
## Cấu trúc cơ bản của tệp docker-compose.yml:
Tệp Docker Compose sử dụng cú pháp YAML và thường bao gồm các phần chính sau
```bash
version: "3.8"
services:
  <service_name>:
    image: <image_name>
    container_name: <container_name>
    ports:
      - "<host_port>:<container_port>"
    environment:
      - <KEY>=<VALUE>
    volumes:
      - <host_path>:<container_path>
    depends_on:
      - <other_service>
    networks:
      - <network_name>
networks:
  <network_name>:
    driver: bridge
volumes:
  <volume_name>:
```
#### 1. Version: 
Xác định phiên bản của cú pháp Docker Compose (ví dụ: 3.8, 3.9). Nên chọn phiên bản phù hợp với phiên bản Docker bạn đang sử dụng.
#### 2. Services: 
- Định nghĩa các container (dịch vụ) sẽ chạy, bao gồm image, port, environment, volume, v.v.

- Mỗi service đại diện cho một container. Các thuộc tính phổ biến:
  - **image**: Tên image Docker (từ Docker Hub hoặc tự build).
  - **build**: Nếu muốn build image từ Dockerfile, chỉ định đường dẫn
  ```bash
  build:
    context: .
    dockerfile: Dockerfile
  ```
  - **container_name**: Tên tùy chỉnh cho container.
  - **ports**: Ánh xạ cổng giữa host và container.
  ```bash
  ports:
    "8080:80" # host:container
  ```
  - **environment**: Biến môi trường cho container
  ```bash
  environment:
    DB_HOST=database
    API_KEY=xyz123
  ```
  Hoặc
  ```bash
  environment:
    DB_HOST: database
    API_KEY: xyz123
  ```
  - **env_file**: Nạp biến môi trường từ tệp:
  ```bash
  env_file:
    .env
  ```
  - **volumes**: Ánh xạ thư mục hoặc volume để lưu trữ dữ liệu.
  ```bash
  volumes:
    ./data:/app/data
    my_volume:/var/lib/mysql
  ```
  - **depends_on**: Chỉ định thứ tự khởi động (container nào cần chạy trước)
  ```bash
  depends_on:
    database
  ```
  - **restart**: Chính sách khởi động lại (no, always, on-failure, unless-stopped).
  ```bash
  restart: always
  ```
  - **networks**: Chỉ định mạng mà container sử dụng.
  ```bash
  networks:
    my_network
  ```

#### 3. Networks (optional): 
- Định nghĩa các mạng tùy chỉnh để cách ly hoặc kết nối các container.
- Driver phổ biến: bridge (mặc định), host, overlay.
```bash
networks:
  my_network:
    driver: bridge
```
#### 4. Volumns (optional): 
- Định nghĩa volume để lưu trữ dữ liệu bền vững.
- Có thể là volume được quản lý bởi Docker hoặc ánh xạ thư mục.
```bash
volumes:
  my_volume:
```
#### 5. Config/Secrets (optional): 
- Quản lý cấu hình hoặc thông tin nhạy cảm.

#### 6. Ví dụ cụ thể
```bash
version: "3.8"

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: web_app
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DB_HOST=database
      - REDIS_HOST=redis
    depends_on:
      - database
      - redis
    volumes:
      - ./src:/app/src
    networks:
      - app_network
    restart: always

  database:
    image: mysql:8.0
    container_name: mysql_db
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: myapp
      MYSQL_USER: user
      MYSQL_PASSWORD: password
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - app_network
    restart: unless-stopped

  redis:
    image: redis:7.0
    container_name: redis_cache
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    networks:
      - app_network
    restart: unless-stopped

networks:
  app_network:
    driver: bridge

volumes:
  db_data:
  redis_data:
```

- **web**:
  - Build từ Dockerfile trong thư mục hiện tại.
  - Ánh xạ cổng 3000 (host) sang 3000 (container).
  - Sử dụng biến môi trường để kết nối với database và redis.
  - Ánh xạ thư mục ./src vào /app/src để phát triển.
- **database**:
  - Sử dụng image mysql:8.0.
  - Cấu hình biến môi trường cho MySQL (user, password, database).
  - Lưu dữ liệu vào volume db_data.
- **redis**:
  - Sử dụng image redis:7.0.
  - Lưu trữ dữ liệu cache vào volume redis_data.
- **networks**:
  - Tất cả container kết nối qua mạng app_network để giao tiếp (ví dụ: web truy cập database qua tên database).
- **volumes**:
  - Tạo hai volume để lưu trữ dữ liệu của MySQL và Redis.

## Các câu lệnh tương tác với file docker-compose.yml
#### 1. Khởi động container: 
```bash
docker-compose up -d # -d: Chạy ở chế độ nền
```
#### 2. Kiểm tra trạng thái: 
```bash
docker-compose ps
```
#### 3. Xem log: 
```bash
docker-compose logs
```
#### 4. Dừng và xóa container: 
```bash
docker-compose down
```
#### 5. Build lại nếu có thay đổi: 
```bash
docker-compose up --build
```