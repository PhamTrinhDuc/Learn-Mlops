#### Playbook, Play, Tasks

| Thuật ngữ    | Ý nghĩa                                                           |
| ------------ | ----------------------------------------------------------------- |
| **Playbook** | Tập hợp các bước tự động hóa                                      |
| **Play**     | Một khối thao tác cho một nhóm máy                                |
| **Task**     | Một hành động đơn lẻ (ví dụ: cài gói, copy file, restart service) |


#### Playbook, Play

| **Tiêu chí**  | **Playbook**                         | **Play**                                      |
| ------------- | ------------------------------------ | --------------------------------------------- |
| Bản chất      | Là **file YAML**                     | Là **một phần bên trong playbook**            |
| Vai trò       | Tập hợp toàn bộ kế hoạch tự động hóa | Mô tả cụ thể việc chạy tasks trên host cụ thể |
| Số lượng      | Một playbook có **nhiều play**       | Một play chỉ thuộc **một playbook**           |
| Gồm những gì? | Danh sách các `play`                 | `hosts`, `tasks`, `vars`, `become`, ...       |

#### Command: 
- Run playbook: 
```bash
ansible-playbook file.yml
```
- Chạy từng task: 
```bash
ansible-playbook create_compute_instance.yml --tags instance1
```
- Check logs: 
```bash
ansible-playbook create_compute_instance.yml -vvv
```