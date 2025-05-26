#### I. Setup Compute engine trên GCP
- Sau khi tạo được VM Instances: 
  - Tìm tới Setting => Metadata => SSH Keys => Add metadata 
  - Trên Terminal gõ: 
  ```bash
  ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  # or 
  ssh-gen
  ```
  - Có 2 dòng suất hiện: 
  ```bash
  Your identification has been saved in /home/ducpham/.ssh/id_ed25519 # private key
  Your public key has been saved in /home/ducpham/.ssh/id_ed25519.pub # public key
  ```
  - Lấy public key và add vào metadata
  ```bash
  cat /home/ducpham/.ssh/id_ed25519.pub
  ```

#### I.1 Config file ssh để connect với VM : 
- Sử dụng GUI: 
  - 1. Cài extention remote ssh
  - 2. Click biểu tượng màu xanh góc trái dưới màn hình
  - 3. Chọn Connect to host
  - 4. Chọn Configurute SSH Hosts
  - 5. Thêm: 
  ```bash
  Host mlops
    HostName External_ip
    User ducpham
    IdentityFile C:\Users\Admin\.ssh\id_ed25519
  ```
- 6. Sử dụng terminal: 
  ```bash
  # Mở file 
  nano ~/.ssh/config
  # Thêm vào file => Ctrl O => Ctrl X
  Host mlops
    HostName External_ip
    User ducpham
    IdentityFile /home/ducpham.ssh/id_ed25519.pub
  ```
- 7. Copy public key từ WSL sang Window: 
  ```bash
  cp ~/.ssh/id_ed25519 /mnt/c/Users/Admin/.ssh/id_ed25519
  cp ~/.ssh/id_ed25519.pub /mnt/c/Users/Admin/.ssh/id_ed25519.pub
  ```

### II. Setup Kubernetes trên GCP
- 1. Switch qua Standard
- 2. Trong Cluster basics: 
  - 2.1 Đặt tên cho cluster
  - 2.2 Location type: chọn Zonal + Zone: asia-southeast1-a
- 3. Trong default=pool: 
  - 3.1 Setup số lượng nodes: 2
  - 3.2 Trong Nodes: chọn machine E2; Machine type: Standard + e2-standard-4; Disk: 100GB

#### II.1 Setup dưới local để thao tác với kubernetes trên cloud: 
```bash
# install gcloud
sudo snap install google-cloud-cli --classic
# login to account
gcloud auth login
# or 
gcloud auth activate-service-account --key-file=/path/to/key.json
```
#### II.2 Lấy file Json của service account trên GCP để login
- 1. Vào menu IAM & Admin > Service Accounts > tạo service account
- 2. Click vào 3 chấm (menu) bên phải service account đó > Chọn Manage keys > Trong phần Keys, nhấn nút ADD KEY > Create new key > Chọn kiểu JSON rồi nhấn CREATE.


### III. Tạo tường lửa trên GCP 
- 1. Search: firewall > Click firewall (VPC Network) > Create a firewall rule  
- 2. Crate firewall
  - 2.1: Đặt tên: allow-port-32434
  - 2.2: Targets: Choose ```All instances in the network```
  - 2.3: Source filters: 0.0.0.0/0
  - 2.4: Protocols and ports > TCP: 32434