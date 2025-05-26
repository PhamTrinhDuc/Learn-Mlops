#### Tạo Compute engine trên Cloud
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

### Config file ssh để connect: 
- Sử dụng GUI: 
  - Cài extention remote ssh
  - Click biểu tượng màu xanh góc trái dưới màn hình
  - Chọn Connect to host
  - Chọn Configurute SSH Hosts
  - Thêm: 
  ```bash
  Host mlops
    HostName External_ip
    User ducpham
    IdentityFile C:\Users\Admin\.ssh\id_ed25519
  ```
- Sử dụng terminal: 
  ```bash
  # Mở file 
  nano ~/.ssh/config
  # Thêm vào file => Ctrl O => Ctrl X
  Host mlops
    HostName External_ip
    User ducpham
    IdentityFile /home/ducpham.ssh/id_ed25519.pub
  ```

- Copy public key từ WSL sang Window: 
```bash
cp ~/.ssh/id_ed25519 /mnt/c/Users/Admin/.ssh/id_ed25519
cp ~/.ssh/id_ed25519.pub /mnt/c/Users/Admin/.ssh/id_ed25519.pub
```


