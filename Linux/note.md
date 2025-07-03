#### 1. Kiểm tra quyền sở hữu thư mục
```bash
ls -ld ./6-storage-persistent
```
### 2. Trả quyền sở hữu cho người dùng hiện tại: 
```bash
sudo chown -R $USER:$USER .
```
#### 3. Cấp quyền ghi cho thư mục: 
```bash
chmod u+rwx /path/to/folder
```
#### 4. Cấp quyền đọc ghi cho tất cả người dùng 
```bash
chmod 777 /path/to/folder
# 
sudo chmod 777 /path/to/folder
```
#### 5. Đổi quyền sở hữu 
```bash
sudo chown your_user_name ./6-storage-persistent
```
#### 6. Tắt port đang chạy: 
```bash
sudo lsof -i :8000
sudo kill -9 PID
```