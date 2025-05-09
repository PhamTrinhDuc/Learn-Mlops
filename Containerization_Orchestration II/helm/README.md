### 0. Install helm:
```bash
sudo snap install helm --classic
```

### 1. Định nghĩa
Helm là trình quản lý package cho Kubernetes, giống như apt/yum/pip nhưng dành cho K8s.
Helm giúp bạn:
- Cài đặt nhanh ứng dụng (PostgreSQL, nginx, Prometheus…)
- Tùy biến cấu hình bằng biến
- Quản lý version và rollback

### 2. Cấu trúc 1 Helm Chart:
```bash
mychart/
├── Chart.yaml          # Thông tin chart
├── values.yaml         # Biến mặc định
└── templates/          # Các file YAML có {{ }} để render
    ├── deployment.yaml
    ├── service.yaml
    └── _helpers.tpl    # File chứa các hàm tái sử dụng
```

## How-to Guid
```shell
cd ocr_chart
helm upgrade --install ocr .
# 1. helm: Gọi công cụ Helm.
# 2. upgrade --install: Nếu release ocr đã tồn tại thì nâng cấp (upgrade); nếu chưa có thì cài đặt mới (install). Đây là cách triển khai idempotent – an toàn để dùng trong CI/CD.
# 3. ocr: Tên của Helm release – bạn đặt tên cho lần cài đặt này là ocr. Sau này có thể dùng lệnh helm list, helm uninstall ocr, v.v.
# 4. ".": Đường dẫn tới chart Helm cần triển khai. Dấu chấm . nghĩa là "chart nằm trong thư mục hiện tại".
```