#!bin/bash

# mode -n: user enter ngay trên dòng echo mà không xuống dòng
echo -n "Do you want to install the script? (y/n): " 
# mode -r: đọc dòng mà không xử lý escape characters (character: "\")
read -r answer

# 1. ${answer}: Đây là cách tham chiếu đến giá trị của biến answer. Dấu ngoặc kép " " được sử dụng để đảm bảo rằng giá trị của biến được xử lý như một chuỗi duy nhất, ngay cả khi nó chứa khoảng trắng hoặc ký tự đặc biệt.
# 2. ,,: Đây là một pattern modifier trong Bash, dùng để chuyển đổi tất cả các ký tự trong chuỗi thành chữ thường.
#   Nếu chỉ sử dụng một dấu phẩy ,, nó sẽ chỉ chuyển ký tự đầu tiên của chuỗi thành chữ thường.
#   Hai dấu phẩy ,, sẽ chuyển toàn bộ chuỗi thành chữ thường.

if [[ "${answer,,}" == "y" ]]; then
    echo "${answer,,}"
    echo "Installing the script..."
else
    echo "Installation cancelled."
fi