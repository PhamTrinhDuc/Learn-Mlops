## 1. Định nghĩa:
Kubernetes (thường được gọi là K8s) là một nền tảng mã nguồn mở để tự động hóa việc triển khai, mở rộng và quản lý các ứng dụng được container hóa. Kubernetes giúp quản lý các container trên nhiều máy chủ, đảm bảo tính sẵn sàng cao, khả năng mở rộng và phục hồi tự động.

## 2. Các khái niệm cơ bản:
- **Cluster**: Một tập hợp các máy chủ (nodes) chạy Kubernetes, bao gồm:
  - Master Node: Quản lý và điều phối cluster (chạy API server, controller manager, scheduler, etcd)
  - Worker Node: Chạy các container ứng dụng
- **Pod**: Đơn vị nhỏ nhất trong Kubernetes, chứa một hoặc nhiều container chia sẻ tài nguyên (network, storage).
- **Deployment**: Quản lý các Pod, đảm bảo số lượng bản sao (replicas) mong muốn luôn chạy.
- **Service**: Định nghĩa cách truy cập các Pod (thông qua tên hoặc địa chỉ IP nội bộ).
- **ConfigMap/Secret**: Lưu trữ cấu hình hoặc thông tin nhạy cảm để cung cấp cho Pod.
- **Namespace**: Phân vùng logic trong cluster để cô lập tài nguyên.
- **Volume**: Lưu trữ dữ liệu bền vững cho Pod, có thể là cục bộ hoặc từ các nhà cung cấp đám mây.

## 3. Cấu trúc cơ bản của tệp biểu mẫu Kubernetes (YAML)
### 3.1 Tệp YAML được sử dụng để định nghĩa các tài nguyên Kubernetes (Pod, Deployment, Service, v.v.). Cấu trúc chung bao gồm:
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
### 3.2 Các thành phần chính trong tệp YAML:
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
  - Chi tiết các thành phần trong spec:
    #### **4.1. Replicas: 3**
      - Ý nghĩa: Chỉ định số lượng bản sao (Pod) mà Deployment cần duy trì. Trong trường hợp này, Kubernetes sẽ đảm bảo luôn có 3 Pod đang chạy ứng dụng.
      - Cách hoạt động: Nếu một Pod bị lỗi hoặc bị xóa, Kubernetes sẽ tự động tạo một Pod mới để duy trì số lượng replicas là 3.
      - Ứng dụng: Điều này hỗ trợ tính sẵn sàng cao (high availability) và khả năng mở rộng (scalability). Bạn có thể dùng lệnh kubectl scale để thay đổi số lượng replicas:
      ```bash
      kubectl scale deployment my-app-deployment --replicas=5
      ```
    #### **4.2. Selector:**
      - ý nghĩa: Xác định cách Deployment tìm và quản lý các Pod mà nó chịu trách nhiệm.
      - Cấu trúc: 
      ```bash
      selector:
        matchLabels:
          app: my-app
      ```
      - matchLabels: Là một bộ lọc dựa trên nhãn (labels) để xác định Pod nào thuộc về Deployment này. Ở đây, Deployment sẽ quản lý tất cả các Pod có nhãn app: my-app.
      - Cách hoạt động: 
        > Deployment sử dụng selector để liên kết với các Pod được tạo ra từ template (xem phần tiếp theo).
        > Nếu có Pod nào khác trong cluster có nhãn app: my-app nhưng không được tạo bởi Deployment này, chúng sẽ không được quản lý bởi Deployment.
    #### **4.3. template:**
      - Định nghĩa mẫu (blueprint) cho các Pod mà Deployment sẽ tạo ra. Mỗi khi cần tạo Pod mới (do mở rộng hoặc thay thế Pod bị lỗi), Kubernetes sẽ sử dụng mẫu này.
      - Cấu trúc: 
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
      - template có hai thành phần chính:
        - **template.metadata**: Định nghĩa thông tin mô tả cho Pod (như nhãn)
        - Cấu trúc: 
        ```bash
        metadata:
          labels:
            app: my-app
        ```
          - labels: Gán nhãn app: my-app cho Pod. Nhãn này được sử dụng để: 
            - Liên kết Pod với Deployment (qua selector.matchLabels).
            - Cho phép các tài nguyên khác (như Service) tìm Pod thông qua nhãn.
        - **template.spec**: Mô tả cấu hình chi tiết của Pod, bao gồm các container chạy trong Pod, cổng, tài nguyên, và các cấu hình khác.
        - Cấu trúc: 
        ```bash
        spec:
          containers:
          - name: my-container
            image: my-app:1.0
            ports:
            - containerPort: 8080
        ```
          - containers: Một danh sách các container chạy trong Pod. Mỗi Pod có thể chứa một hoặc nhiều container, nhưng trong trường hợp này chỉ có một container.
          - Chi tiết các trường trong container: 
            - *name: my-container*:
              - Đặt tên cho container (phải duy nhất trong Pod).
              - Tên này được sử dụng để tham chiếu container khi xem log hoặc thực thi lệnh (kubectl logs, kubectl exec).
            - *image: my-app:1.0:*
              - Chỉ định image Docker để chạy container.
              - Ở đây, container sử dụng image my-app với tag 1.0 (có thể được kéo từ Docker Hub hoặc registry khác).
              - Kubernetes sẽ kéo image này từ registry nếu nó chưa có trên node.
            - *ports:*
              - Chỉ định các cổng mà container sẽ lắng nghe.
              - Trường containerPort: 8080 cho biết container mở cổng 8080.
              - Lưu ý: Đây chỉ là thông tin mô tả, không tự động ánh xạ cổng ra ngoài. Để truy cập cổng này từ bên ngoài, bạn cần một Service (như ClusterIP, NodePort, hoặc LoadBalancer).
        - Các trường khác có thể thêm vào: 
          - env: Định nghĩa biến môi trường
          ```bash
          env:
            - name: DB_HOST
              value: "mysql-service"
          ```
          - resources: Giới hạn tài nguyên CPU và RAM:
          ```bash
          resources:
            limits:
              cpu: "500m"
              memory: "512Mi"
            requests:
              cpu: "200m"
              memory: "256Mi"
          ```
## 4. Các tài nguyên phổ biến
### 4.1 Pod: 
- Đơn vị nhỏ nhất, chứa một hoặc nhiều container
- Ví dụ: 
```bash
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  labels:
    app: my-app
spec:
  containers:
  - name: my-container
    image: nginx:1.14
    ports:
    - containerPort: 80
```
### 4.2 Deployment
- Quản lý Pod, đảm bảo số lượng bản sao, hỗ trợ cập nhật và rollback.
- Ví dụ: 
```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-deployment
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
      - name: my-app
        image: my-app:1.0
        ports:
        - containerPort: 8080
        env:
        - name: DB_HOST
          value: "mysql-service"
```
### 4.3 Service
- Cung cấp địa chỉ cố định để truy cập Pod.
- Các loại: ClusterIP (mặc định), NodePort, LoadBalancer.
- Ví dụ: 
```bash
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  selector:
    app: my-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: ClusterIP
```
### 4.4 ConfigMap
- Lưu trữ cấu hình không nhạy cảm.
- Ví dụ: 
```bash
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-config
data:
  app.properties: |
    db.host=mysql-service
    log.level=debug
```
### 4.5 Secret
- Lưu trữ thông tin nhạy cảm
- Ví dụ: 
```bash
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
type: Opaque
data:
  db-password: cGFzc3dvcmQ= # Base64 encoded
```
### 4.6 Ingress
- Quản lý truy cập HTTP/HTTPS từ bên ngoài vào Service.
- Yêu cầu Ingress Controller (như NGINX, Traefik).
```bash
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: my-app-service
            port:
              number: 80
```
### Ví dụ cụ thể: 
- Dưới đây là một bộ manifest YAML cho một ứng dụng web với Deployment, Service và ConfigMap:
```bash
# Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  template:
    metadata:
      labels:
        app: web-app
    spec:
      containers:
      - name: web-container
        image: web-app:1.0
        ports:
        - containerPort: 3000
        env:
        - name: NODE_ENV
          value: "production"
        - name: CONFIG_KEY
          valueFrom:
            configMapKeyRef:
              name: app-config
              key: app.key
---
# Service
apiVersion: v1
kind: Service
metadata:
  name: web-app-service
  namespace: default
spec:
  selector:
    app: web-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: ClusterIP
---
# ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
  namespace: default
data:
  app.key: "value123"
```

## 5. Các câu lệnh với kubernetes
- Sử dụng công cụ kubectl để quản lý tài nguyên Kubernetes.
### 5.1 Áp dụng manifest YAML:
```bash
kubectl apply -f <filename>.yaml
```
### 5.2 Kiểm tra trạng thái tài nguyên:
- Xem Pod: 
```bash
kubectl get pods
```
- Xem Deployment
```bash
kubectl get deployments
```
- Xem Service
```bash
kubectl get services
```
### 5.3 Xem chi tiết tài nguyên:
```bash
kubectl describe <resource_type> <resource_name>
# kubectl describe pod my-pod
```
### 5.4 Xem log của Pod:
```bash
kubectl logs <pod_name> 
# kubectl logs web-app-pod
```
### 5.5 Xóa tài nguyên:
```bash
kubectl delete -f <filename>.yaml 
# or
kubectl delete <resource_type> <resource_name>
# kubectl delete deployment web-app
```
### 5.6 Mở rộng hoặc thu hẹp Deployment:
```bash
kubectl scale deployment <deployment_name> --replicas=<number>
# kubectl scale deployment web-app --replicas=5
```
### 5.7 Cập nhật image trong Deployment:
```bash
kubectl set image deployment/<deployment_name> <container_name>=<new_image>
# kubectl set image deployment/web-app web-container=web-app:2.0
```
### 5.8 Truy cập shell trong Pod:
```bash
kubectl exec -it <pod_name> -- /bin/bash
# or use sh
kubectl exec -it <pod_name> -- /bin/sh
```
## 6. So sánh Docker-compose với Kubernetes
### Điểm tương đồng:
- Quản lý container: Cả hai đều dùng để định nghĩa và chạy các container (như ứng dụng web, database).
-  Cấu hình declaratively: Sử dụng tệp YAML để mô tả các thành phần (services, volumes, networks trong Docker Compose; pods, services, deployments trong Kubernetes).
- Tự động hóa: Cả hai hỗ trợ tự động hóa việc triển khai và quản lý container.
### Điểm khác:
| **Tiêu chí**     | **Docker Compose**                                           | **Kubernetes**                                                           |
|------------------|--------------------------------------------------------------|---------------------------------------------------------------------------|
| **Mục đích**      | Quản lý container trên một máy hoặc cụm nhỏ.                | Quản lý container trên cụm lớn, phân tán.                                |
| **Quy mô**        | Phù hợp cho dev, test, hoặc dự án nhỏ.                      | Phù hợp cho sản phẩm lớn, cần scale, HA.                                 |
| **Tính năng**     | Đơn giản, dễ dùng, ít tính năng phức tạp.                   | Hỗ trợ auto-scaling, self-healing, rolling updates.                      |
| **Networking**    | Mạng đơn giản (bridge, host).                               | Mạng phức tạp, tích hợp service discovery, load balancing.              |
| **Triển khai**    | Chạy cục bộ hoặc trên một server.                           | Chạy trên cụm (nhiều node), cần thiết lập cluster.                      |
| **Công cụ**       | Chỉ cần Docker.                                              | Cần cụm Kubernetes (Minikube, EKS, GKE, AKS).                            |
