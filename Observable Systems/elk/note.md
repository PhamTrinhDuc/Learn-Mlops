### Thành phần của ELK Stack: 

| Thành phần        | Vai trò                  | Mô tả chi tiết                                                                                                                                                  |
| ----------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Elasticsearch** | **Lưu trữ & tìm kiếm**   | Một công cụ tìm kiếm và phân tích dựa trên Lucene, giúp lưu trữ và truy vấn dữ liệu log theo thời gian thực.                                                    |
| **Logstash**      | **Thu thập & xử lý log** | Một pipeline xử lý dữ liệu, giúp lấy log từ nhiều nguồn (file, syslog, Kafka,...) rồi chuyển đổi dữ liệu thành định dạng chuẩn trước khi gửi đến Elasticsearch. |
| **Kibana**        | **Trực quan hóa**        | Giao diện web dùng để tạo dashboard, biểu đồ, truy vấn và phân tích dữ liệu lưu trữ trong Elasticsearch.                                                        |

## Cấu trúc Project ELK Stack

### 1. Cấu hình chính:
- **`.env`**: Chứa các biến môi trường cho toàn bộ stack
  - `ELASTIC_VERSION=8.4.1`
  - Mật khẩu cho các user: `elastic`, `logstash_internal`, `kibana_system`
- **`elk-docker-compose.yml`**: File chính để khởi động toàn bộ ELK stack

### 2. Các thành phần chính:

#### **Elasticsearch** (`/elasticsearch/`)
- **Dockerfile**: Sử dụng base image `docker.elastic.co/elasticsearch/elasticsearch`
- **Config**: `elasticsearch.yml`
  - Cluster name: `docker-cluster`
  - Network host: `0.0.0.0`
  - X-Pack security: disabled
  - License type: trial

#### **Kibana** (`/kibana/`)
- **Dockerfile**: Sử dụng base image `docker.elastic.co/kibana/kibana`
- **Config**: `kibana.yml`
  - Server host: `0.0.0.0`
  - Elasticsearch hosts: `http://elasticsearch:9200`
  - Credentials: `kibana_system` user

#### **Setup** (`/setup/`)
- **Mục đích**: Khởi tạo users và roles cho Elasticsearch
- **Entrypoint script**: `entrypoint.sh`
- **Helper functions**: `helpers.sh`
- **Roles**: `logstash_writer.json` với quyền:
  - Cluster: `manage_index_templates`, `monitor`, `manage_ilm`
  - Indices: quyền `write`, `create`, `manage` cho logstash indexes

### 3. Extensions:

#### **Filebeat** (`/extensions/filebeat/`)
- **Mục đích**: Thu thập logs từ Docker containers
- **Config**: `filebeat.yml`
  - Docker autodiscover enabled
  - Output tới Elasticsearch
  - HTTP endpoint cho health checking
- **Compose file**: `filebeat-compose.yml`
  - Chạy với user `root`
  - Mount Docker socket và container logs
  - Kết nối với Elasticsearch qua network `elk`

### 4. Cách sử dụng:

#### Khởi động ELK Stack cơ bản:
```bash
docker compose -f elk-docker-compose.yml up -d
```

#### Khởi động với Filebeat:
```bash
docker compose -f elk-docker-compose.yml -f extensions/filebeat/filebeat-compose.yml up -d
```

#### Truy cập các services:
- **Elasticsearch**: http://localhost:9200
- **Kibana**: http://localhost:5601

### 5. Workflow hoạt động:

1. **Setup service**: Tạo users và roles trong Elasticsearch
2. **Elasticsearch**: Lưu trữ và index dữ liệu log
3. **Kibana**: Giao diện web để truy vấn và visualize
4. **Filebeat** (optional): Thu thập logs từ Docker containers

### 6. Security Configuration:

#### Users được tạo tự động:
- **elastic**: Superuser với full access
- **kibana_system**: User cho Kibana kết nối với Elasticsearch  
- **logstash_internal**: User cho Logstash ghi dữ liệu

#### Roles:
- **logstash_writer**: Quyền ghi và quản lý logstash indices

### 7. Volumes và Networks:

#### Volumes:
- `setup`: Lưu trạng thái setup
- `elasticsearch`: Persistent data cho Elasticsearch

#### Network:
- `elk`: Bridge network cho tất cả services

### 8. Environment Variables:

```bash
ELASTIC_VERSION=8.4.1
ELASTIC_PASSWORD=changeme
LOGSTASH_INTERNAL_PASSWORD=changeme  
KIBANA_SYSTEM_PASSWORD=changeme
```

### 9. Ports được expose:

| Service       | Port Host | Port Container | Mô tả                    |
| ------------- | --------- | -------------- | ------------------------ |
| Elasticsearch | 9200      | 9200           | REST API                 |
| Elasticsearch | 9300      | 9300           | Transport (cluster comm) |
| Kibana        | 5601      | 5601           | Web interface           |

### 10. Lưu ý quan trọng:

- **Initial setup**: Service `setup` chỉ chạy lần đầu để khởi tạo users
- **Security**: X-Pack security hiện tại đang disabled
- **Data persistence**: Elasticsearch data được lưu trong Docker volume
- **Resource**: ES Java heap được set là 512MB (phù hợp cho development)
- **Discovery**: Single node mode (không dành cho production cluster)

### 11. Một hệ thống ELK chuẩn thường thu thập:

| Loại log         | Nguồn             | Dụng cụ                     |
| ---------------- | ----------------- | --------------------------- |
| Application logs | stdout / file     | loguru / winston / logback  |
| Container logs   | Docker            | Filebeat `container` input  |
| Web logs         | Nginx, Apache     | Filebeat `nginx` module     |
| System logs      | Linux             | Filebeat `system` module    |
| Database logs    | MySQL, PostgreSQL | Filebeat module hoặc manual |
| Audit logs       | App hoặc OS       | Custom log hoặc `auditd`    |
