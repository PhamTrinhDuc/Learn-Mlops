### Các service có trong file `prom-grafa-docker-compose.yml`

| **Service**     | **Ứng dụng chính**                  | **Mô tả chi tiết**                                                                                                                                                                | **Liên kết với các service khác**                                                                                          |
| --------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `node-exporter` | Export metric hệ thống máy chủ      | Thu thập thông tin về CPU, RAM, Disk, Network từ máy chủ cục bộ.                                                                                                                  | Gửi metrics đến `prometheus`.                                                                                              |
| `prometheus`    | Thu thập & lưu trữ dữ liệu giám sát | Là trung tâm hệ thống monitoring, truy vấn các metrics định kỳ từ `node-exporter`, `cadvisor`, `demo-metrics`,... và lưu trữ chúng dưới dạng time-series.                         | Lấy dữ liệu từ exporters (như `node-exporter`, `cadvisor`), gửi alert đến `alertmanager`, làm nguồn dữ liệu cho `grafana`. |
| `alertmanager`  | Hệ thống gửi cảnh báo               | Nhận alert từ `prometheus` khi một rule cảnh báo được kích hoạt (ví dụ CPU > 90%), sau đó gửi thông báo qua email, Slack, v.v.                                                    | Nhận cảnh báo từ `prometheus`.                                                                                             |
| `cadvisor`      | Theo dõi container                  | Thu thập metrics về hiệu suất và trạng thái của container Docker (CPU, memory, I/O, network).                                                                                     | Export dữ liệu cho `prometheus` như `node-exporter`.                                                                       |
| `grafana`       | Hiển thị dữ liệu trực quan          | Tạo dashboard từ các dữ liệu lấy từ `prometheus`, vẽ biểu đồ, bảng thống kê, gauge,...                                                                                            | Lấy dữ liệu từ `prometheus`, đôi khi từ `alertmanager`.                                                                    |
| `jaeger`        | Phân tích trace, theo dõi request   | Là công cụ theo dõi phân tán (distributed tracing), giúp biết được các request đi qua service nào, mất bao lâu. Dùng cho debugging hiệu suất hệ thống vi dịch vụ (microservices). | Có thể dùng chung với `grafana`, không liên quan trực tiếp đến `prometheus` nhưng bổ trợ cho hệ observability.             |


### Luồng hoạt động

```bash
[ node-exporter ]     [ cadvisor ]      [ demo-metrics ]
         │                  │                    │
         └──────┬───────────┴──────────────┐
                │                      [ jaeger ]
          [ prometheus ]                ↑
                │                       │
         [ alertmanager ]         (optional integration)
                │
         [ Email / Slack ]
                ↓
           [ grafana ]
    (visualize everything above)
```