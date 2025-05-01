
## Định nghĩa:
Docker Compose là một công cụ để định nghĩa và chạy các ứng dụng Docker đa container bằng cách sử dụng tệp cấu hình YAML. Tệp docker-compose.yml được sử dụng để mô tả các service, network, volume và các cấu hình khác
## Cấu trúc cơ bản của tệp docker-compose.yml:
Tệp Docker Compose sử dụng cú pháp YAML và thường bao gồm các phần chính sau
#### 1. Version: 
Xác định phiên bản của cú pháp Docker Compose (ví dụ: 3.8, 3.9). Nên chọn phiên bản phù hợp với phiên bản Docker bạn đang sử dụng.
#### 2. Services: 
- Định nghĩa các container (dịch vụ) sẽ chạy, bao gồm image, port, environment, volume, v.v.

- Mỗi service đại diện cho một container. Các thuộc tính phổ biến:
  - image: Tên image Docker (từ Docker Hub hoặc tự build).
  - build: Nếu muốn build image từ Dockerfile, chỉ định đường dẫn
  '''bash
  build:
  context: .
  dockerfile: Dockerfile
  '''
  - container_name: Tên tùy chỉnh cho container.
  - ports: Ánh xạ cổng giữa host và container.
  '''bash
  ports:
  - "8080:80" # host:container
  '''
  - environment: Biến môi trường cho container
  '''bash
  environment:
  - DB_HOST=database
  - API_KEY=xyz123
  '''
  Hoặc
  '''bash
  environment:
  DB_HOST: database
  API_KEY: xyz123
  '''
#### 3. Networks (optional): 
Cấu hình các mạng tùy chỉnh để các container giao tiếp với nhau.
#### 4. Volumns (optional): 
Định nghĩa các volume để lưu trữ dữ liệu bền vững.
#### 5. Config/Secrets (optional): 
Quản lý cấu hình hoặc thông tin nhạy cảm.

#### 6. Cú pháp cơ bản: 
'''bash
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
'''