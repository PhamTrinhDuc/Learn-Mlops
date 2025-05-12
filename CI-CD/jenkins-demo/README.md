### Mục tiêu 
- Một app Flask đơn giản.
- Viết sẵn unit test.
- Jenkins sẽ:
  - Pull code từ GitHub.
  - Cài dependencies.
  - Chạy test.
  - Build Docker image.
  - Chạy container (giả lập deploy).

### Cấu trúc:
```bash
python-demo/
├── app/
│   ├── main.py
│   └── requirements.txt
├── tests/
│   └── test_main.py
├── Dockerfile
└── Jenkinsfile
```

### Jenkins làm gì ở mỗi bước: 
| Giai đoạn            | Jenkins làm gì?                                  |
| -------------------- | ------------------------------------------------ |
| Clone Code           | Lấy code từ GitHub về workspace                  |
| Install Dependencies | Cài thư viện Python (`flask`)                    |
| Run Tests            | Dùng `pytest` chạy test (fail thì dừng pipeline) |
| Build Docker Image   | Tạo image từ `Dockerfile`                        |
| Run Container        | Chạy app Flask trong Docker container            |

> Nếu không có Jenkins tự động, dev sẽ phải thủ công: 
> 1. Chạy các test thủ công
> 2. Build image và run thành container thủ công

### Lợi ích khi có Jenkins CI-CD: 
| Thủ công                      | Jenkins (CI/CD)              |
| ----------------------------- | ---------------------------- |
| Lặp lại thủ công, dễ sót bước | Tự động, ổn định             |
| Không ai kiểm tra chất lượng  | Có test, fail thì rollback   |
| Mất thời gian deploy          | Deploy chỉ vài giây          |
| Không đồng bộ giữa dev        | Tất cả cùng theo 1 quy trình |

### Làm sao để pytest biết đâu là test ?
> File phải có tên bắt đầu với test_ hoặc kết thúc bằng _test.py.
> Hàm phải có tên bắt đầu bằng test_ .

### Note: 
> Jenkins/jenkins:lts image không có sẵn docker cli
> Cần cài đặt docker cli để sử dụng docker trong Jenkins. Sau đó dùng images này để build container cho Jenkins