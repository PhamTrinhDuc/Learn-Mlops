### I. Thêm domain vào file hosts để ánh xạ domain → IP cục bộ - Local DNS Mapping: 
#### 1. Mục tiêu của file /etc/hosts là gì?
File này là nơi máy tính ánh xạ domain thành IP, trước khi hỏi DNS server ngoài internet.
#### 2. Khi bạn thêm vào /etc/hosts như sau:
'''bash
127.0.0.1   rancher.mlops.vn
```
- Bạn đang nói với máy tính: “Này máy ơi, nếu mày thấy ai truy cập rancher.mlops.vn, thì đừng đi hỏi Google DNS, mày cứ chuyển luôn sang 127.0.0.1 (localhost) nhé.”
- Khi bạn gõ vào trình duyệt:
```bash
https://rancher.mlops.vn
```
- Hệ điều hành sẽ:
  - Check trong /etc/hosts xem rancher.mlops.vn trỏ đi đâu
  - Thấy nó trỏ về 127.0.0.1
  - Kết nối đến localhost → gửi HTTP request đến container đang chạy trên máy bạn