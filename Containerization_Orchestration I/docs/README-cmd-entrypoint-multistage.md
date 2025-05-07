
## CMD Và ENTRYPOINT

### CASE 1: Chỉ dùng ENTRYPOINT
```bash
FROM python:3.9-slim
ENTRYPOINT ["echo", "Hello Docker"]
```
- Giải thích:
  - ENTRYPOINT ["echo", "Hello Docker"] chỉ định rằng lệnh echo "Hello Docker" sẽ được chạy khi container khởi động.
  - Vì không có CMD, không có tham số bổ sung nào được cung cấp.
  - Khi chạy container (docker run image), kết quả sẽ là:
    ```bash
    Hello Docker
    ```
  - Nếu bạn truyền thêm tham số khi chạy container (docker run image other args), các tham số này sẽ thay thế toàn bộ ["echo", "Hello Docker"] nếu dùng --entrypoint, hoặc gây lỗi nếu không hợp lệ.
  - Ứng dụng: Dùng khi bạn muốn container hoạt động như một lệnh cụ thể, ví dụ như một script cố định (predict.sh).

### CASE 2: Kết hợp ENTRYPOINT và CMD

```bash
FROM python:3.9-slim
ENTRYPOINT ["echo"]
CMD ["Hello Docker"]
```
- Giải thích: 
  - ENTRYPOINT ["echo"] xác định lệnh chính là echo.
  - CMD ["Hello Docker"] cung cấp tham số mặc định cho ENTRYPOINT. Khi container khởi động, lệnh đầy đủ sẽ là echo "Hello Docker".
  - Kết quả khi chạy docker run image:
  ```bash
  Hello Docker
  ```
  - Nếu bạn truyền thêm tham số khi chạy container (docker run image other args), các tham số này sẽ ghi đè CMD. Ví dụ:
  ```bash
  - docker run image World # Output: World
  ```
  - Ứng dụng: Phổ biến khi bạn muốn cung cấp một lệnh chính (như python predict.py) và cho phép người dùng truyền tham số linh hoạt (như --data data_path).

### CASE 3: Chỉ dùng CMD
```bash
FROM python:3.9-slim
CMD ["echo", "Hello Docker"]
```
- Giải thích: 
  - Không có ENTRYPOINT được chỉ định, Docker sẽ sử dụng entrypoint mặc định là /bin/sh -c.
  - CMD ["echo", "Hello Docker"] sẽ được chạy trong shell, tức là lệnh đầy đủ là /bin/sh -c "echo Hello Docker".
  - Kết quả khi chạy docker run image:
  ```bash
  Hello Docker
  ```
  - Nếu bạn truyền tham số khi chạy container (docker run image other args), tham số này sẽ ghi đè toàn bộ CMD. Ví dụ:
  ```bash
  docker run image echo World # Output: World
  ```
  - Ứng dụng: Thường dùng khi bạn muốn container chạy một lệnh đơn giản và cho phép người dùng dễ dàng thay đổi hành vi bằng cách ghi đè CMD.


## Multistage Build

### Tổng quan: 
- Multi-stage build sử dụng nhiều FROM trong một Dockerfile, mỗi FROM đại diện cho một stage riêng biệt.
- Mỗi stage có thể dựa trên một base image khác nhau và thực hiện các tác vụ riêng (như cài đặt dependencies, biên dịch mã, hoặc cấu hình runtime).
- Các stage có thể sao chép file hoặc artifact từ stage trước đó bằng COPY --from=<stage_name>.
- Stage cuối cùng (thường là runtime) là image được tạo ra, trong khi các stage trước đó bị loại bỏ, giúp giảm kích thước image.

### Lợi ích: 
- Tối ưu kích thước image: Chỉ giữ lại những gì cần thiết cho runtime, loại bỏ các công cụ biên dịch hoặc dependencies không cần thiết.
- Tăng bảo mật: Giảm bề mặt tấn công bằng cách loại bỏ các công cụ không cần thiết trong image cuối.
- Tổ chức rõ ràng: Tách biệt logic biên dịch và runtime.

### Cách hoạt động: 
- Stage 1 (compile-image): Cài đặt các thư viện Python vào /opt/venv trên base image python:3.9-slim.
- Stage 2 (runtime-image): Sao chép /opt/venv từ stage 1, dùng base image nhẹ hơn (python:3.9-alpine), và cấu hình để chạy MLflow server trên cổng 5000.
- Kết quả: Một image nhỏ gọn, chỉ chứa Python, môi trường ảo, và lệnh chạy MLflow server, tối ưu cho triển khai.