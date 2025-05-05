## Định nghĩa:
Kubernetes (thường được gọi là K8s) là một nền tảng mã nguồn mở để tự động hóa việc triển khai, mở rộng và quản lý các ứng dụng được container hóa. Kubernetes giúp quản lý các container trên nhiều máy chủ, đảm bảo tính sẵn sàng cao, khả năng mở rộng và phục hồi tự động.

## Các khái niệm cơ bản:
- **Cluster**: Một tập hợp các máy chủ (nodes) chạy Kubernetes, bao gồm:
  - Master Node: Quản lý và điều phối cluster (chạy API server, controller manager, scheduler, etcd)
  - Worker Node: Chạy các container ứng dụng
- **Pod**: Đơn vị nhỏ nhất trong Kubernetes, chứa một hoặc nhiều container chia sẻ tài nguyên (network, storage).
- **Deployment**: Quản lý các Pod, đảm bảo số lượng bản sao (replicas) mong muốn luôn chạy.
- **Service**: Định nghĩa cách truy cập các Pod (thông qua tên hoặc địa chỉ IP nội bộ).
- **ConfigMap/Secret**: Lưu trữ cấu hình hoặc thông tin nhạy cảm để cung cấp cho Pod.
- **Namespace**: Phân vùng logic trong cluster để cô lập tài nguyên.
- **Volume**: Lưu trữ dữ liệu bền vững cho Pod, có thể là cục bộ hoặc từ các nhà cung cấp đám mây.

## Cấu trúc cơ bản của tệp biểu mẫu Kubernetes (YAML)
### Tệp YAML được sử dụng để định nghĩa các tài nguyên Kubernetes (Pod, Deployment, Service, v.v.). Cấu trúc chung bao gồm:
```bash
apiVersion: <version>
kind: <resource_type>
metadata:
  name: <resource_name>
  namespace: <namespace>
  labels:
    <key>: <value>
spec:
  <resource_specific_config>
```
### Các thành phần chính trong tệp YAML:
  #### **1. apiVersion**: 
  - Chỉ định phiên bản API của Kubernetes được sử dụng.
  - Ví dụ: 
    - v1 cho Pod, Service.
    - apps/v1 cho Deployment.
    - networking.k8s.io/v1 cho Ingress.

  #### **2. kind**: 
  - Loại tài nguyên (Pod, Deployment, Service, ConfigMap, Secret...)
  - Ví dụ: Deployment, Service, Pod.

  #### **3. metadata**
  - Thông tin mô tả tài nguyên: 
    - name: tên duy nhất của tài nguyên
    - namespace: Không gian tên (mặc định là default).
    - labels: Nhãn để lọc hoặc nhóm tài nguyên.
    - Ví dụ: 
    ```bash
    metadata:
    name: my-app
    namespace: production
    labels:
      app: my-app
    ```
  #### **4. spec**
  - Định nghĩa cấu hình cụ thể cho tài nguyên
  - Tùy thuộc vào kind, spec sẽ có các trường khác nhau
  - Ví dụ cho Deployment: 
  ```bash
  spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: my-app:1.0
        ports:
        - containerPort: 8080
  ```
  #### **1. Replicas: 3**
    + Ý nghĩa: Chỉ định số lượng bản sao (Pod) mà Deployment cần duy trì. Trong trường hợp này, Kubernetes sẽ đảm bảo luôn có 3 Pod đang chạy ứng dụng.
    + Cách hoạt động: Nếu một Pod bị lỗi hoặc bị xóa, Kubernetes sẽ tự động tạo một Pod mới để duy trì số lượng replicas là 3.
    + Ứng dụng: Điều này hỗ trợ tính sẵn sàng cao (high availability) và khả năng mở rộng (scalability). Bạn có thể dùng lệnh kubectl scale để thay đổi số lượng replicas:
    ```bash
    kubectl scale deployment my-app-deployment --replicas=5
    ```
  #### **2. Selector:**
    + ý nghĩa: Xác định cách Deployment tìm và quản lý các Pod mà nó chịu trách nhiệm.
    + Cấu trúc: 
    ```bash
    selector:
      matchLabels:
        app: my-app
    ```
    + matchLabels: Là một bộ lọc dựa trên nhãn (labels) để xác định Pod nào thuộc về Deployment này. Ở đây, Deployment sẽ quản lý tất cả các Pod có nhãn app: my-app.
    + Cách hoạt động: 
      > Deployment sử dụng selector để liên kết với các Pod được tạo ra từ template (xem phần tiếp theo).
      > Nếu có Pod nào khác trong cluster có nhãn app: my-app nhưng không được tạo bởi Deployment này, chúng sẽ không được quản lý bởi Deployment.
  #### **3. template:**
    + Định nghĩa mẫu (blueprint) cho các Pod mà Deployment sẽ tạo ra. Mỗi khi cần tạo Pod mới (do mở rộng hoặc thay thế Pod bị lỗi), Kubernetes sẽ sử dụng mẫu này.
    + Cấu trúc: 
    ```bash
    template:
      metadata:
        labels:
          app: my-app
      spec:
        containers:
        - name: my-container
          image: my-app:1.0
          ports:
          - containerPort: 8080
    ```
    + template: chứa hai phần chính: 
      + metadata: Định nghĩa thông tin mô tả cho Pod (như nhãn)
      + Cấu trúc: 
      ```bash
      metadata:
        labels:
          app: my-app
      ```
      + labels: 
      + spec: Định nghĩa cấu hình chi tiết của Pod (như container, cổng, biến env...)

## Các tài nguyên phổ biến

## Các câu lệnh với kubernetes

## So sánh Docker-compose với Kubernetes