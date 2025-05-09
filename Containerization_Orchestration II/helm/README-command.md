### Tạo Helm chart vào Kubernetes cluster: 
```bash
helm upgrade --install ocr .
```
### Xem các release hiện có: 
```bash
helm list
```
### Xem các Helm được tạo: 
```bash
helm history <release-name>
```
### Xóa Helm chart từ RELEASE NAME:
```bash
helm uninstall <release-name>
```
### Rollback lại 1 phiên bản cụ thể: 
```bash
helm history ocr # list ra các helm chart, status=deployed: phiên bản hiện tại
helm rollback ocr 1
# Lưu ý: Khi rollback lại 1 phiên bản, Helm sẽ ghi lại hành động rollback như một "phiên bản mới"
```
### Get Service: 
```bash
kubectl get service
```
### Access service: 
```bash
kubectl port-forward svc/my-app 30000:30000
# open: http://localhost:30000
```