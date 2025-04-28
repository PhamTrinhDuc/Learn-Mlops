#!/bin/bash

FILENAME=$1 # => 1: nhập input đầu tiên vào 
# PORT=$2 # => 2: nhập input thứ 2 vào

# ===================================================================
if [[ "$1" ]]; then
    echo "Watching the file $FILENAME"
    # echo "Port is $PORT"
else
    echo "Mising the file to watch :("
    exit 1
fi
# ===================================================================

#stat:            Lệnh lấy thông tin của file
#-c%s:            Format output chỉ lấy kích thước file (in bytes)
#$FILENAME:       Tên file bạn đang kiểm tra
#$(...):          Gán output vào biến prevSize
#echo $prevSize:  In ra kích thước file
prevSize="$(stat -c%s $FILENAME)"  # For MacOS, replace with -f%z
echo "Previous size: $prevSize"

while true
do 
    currentSize=$(stat - c%s $FILENAME)
    if [[ $currentSize - gt $prevSize]]; then  # -gt : greater than, so sánh 2 số nguyên
        tail -1 "$FILENAME" # tail: lấy dòng cuối cùng của file, -1: lấy 1 dòng
        prevSize=$currentSize
    fi
done