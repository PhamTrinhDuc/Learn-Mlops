## SETUP KUBERNETES VÀ DOCKER CHO CI/CD 
### Requirements: 
- Đã setup cluster trên GCP bằng ansible hoặc terraform
- Đã setup 1 VM trên GCP
### 1. Cài docker trên VM đã tạo
- Mở cổng cho VM nếu không kết nối được: xem cách mở firewall trong bài Cloud
- ssh vào VM 
- Cài docker: 
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```
- Chạy các command sau để cho phép chạy docker mà không cần `sudo`: 
```bash
sudo groupadd docker # Tạo một nhóm Linux có tên docker
sudo usermod -aG docker $USER # Thêm user hiện tại ($USER) vào nhóm docker
newgrp docker # Tải lại nhóm cho phiên đăng nhập hiện tại
```
### 2 Setup container của jenkins trên VM:
#### 2.1 File docker-compose.yml đã custom để cài docker và kubernetes: 
```bash
refactor/custome-images/jenkins/docker-compose.yml
``` 
#### 2.2. Tạo file jenkins-docker-compose.yaml:
```bash
vim jenkins-docker-compose.yaml
I: để insert 
ESC: thoát insert 
:qw: để thoát
```
#### 2.3. Run container : 
```bash
docker compose -f jenkins-docker-compose.yml up -d
```
#### 2.4. Đăng nhập vào jenkins và cài pluggin: 
- Mở cổng 8081 trên GCP 
- Cài pluggin Kubernetes trên Jenkins
#### 2.5. Connect jenkins tới Cluster trên GCP đã tạo: 
- Vào Cluster trên GCP -> Connect -> Paste xuống local để connect tới Cluster
- Quay lại jenkins -> Manage Jenkins -> Cloud -> New Cloud: 
```bash
Name: autopilot-cluster-1
Choose: Kubernets -> New 
```
- Quay lại local: 
```bash
cat ~/.kube/config
```
  - Tìm tới cluster có tên trùng tên trên GCP 
  - Tim tới: 
  ```bash
  server: https://34.126.136.2 => paste vào Kubernetes URL trên Jenkins
  certificate-authority-data: LS0tL... => paste vào Kubernetes server certificate key trên Jenkins
  ```
- Namespace trên Jenkins: model-serving => Test Connection => Failed
#### 2.6 Set quyền cho jenkins để connect với Kubernetes: 

- 1. Tạo ServiceAccount riêng cho Jenkins
```shell
kubectl create serviceaccount jenkins-sa -n model-serving
kubectl create clusterrolebinding jenkins-sa-binding \
  --clusterrole=admin \
  --serviceaccount=model-serving:jenkins-sa
```
- 2. Lấy token của jenkins-sa: 
```bash
kubectl -n model-serving create token jenkins-sa
```
- 3. Quay lại jenkins để thêm Credentials: 
  - Credentials: Add => Jenkins => Kind: Secret text => Secret: paste key từ bước trên => ID: k8s-token => Add. 
  - Credentials: chọn k8s-token
