#### Get namespace:
```bash
kubectl get namespace # or ns => all namspace
```
#### Create namespace:
```bash
kubectl create ns test
```
#### Switch sang namespace:
```bash
kubens test
```
#### Check xem pod nào chạy trên namespace:
```bash
kubectl get pod  # or po => all
kubectl get pod mypod # => chỉ định tên pod
```
#### Tạo pod: 
```bash
kubectl apply -f pod.yaml
```
#### Xem quá trình tạo:
```bash
kubectl describe pod mypod # check Events
```
#### Xem logs:
```bash
kubectl logs mypod
```
#### Xem thông tin pod:
```bash
kubectl get pod mypod -o yaml # or -o json
kubectl get pod mypod -o yaml > mypod.yaml # logs ra file 
```
#### Delete pod:
```bash
kubectl delete pod mypod
```
#### Tạo deployment
```bash
kubectl apply -f deployment.yaml
# lưu ý: tạo deployment ở namespace nào thì phải switch sang namespace đó
```
#### Xem deployment
```bash
kubectl get deployments
```
### Chạy chuỗi lệnh sau:
```bash
kubectl get pod # lấy các pod được tạo từ deployment
kubectl delete pod  mydeployment-747998d9dd-p7dkp # Xóa thử 1 pod đi
kubectl get pod # Vẫn thấy 2 pod vì deployment đã tạo lại để đảm bảo đủ 2 pod (replicas: 2)
```
### Get replicas:
```bash
kubectl get replicasets # or kbectl get rs
# Lưu ý: + Deployment tạo replicas sau đó replicas mới tạo pod
#        + Tương tự khi với pod, khi xóa replicas thì replicas sẽ tự được tạo lại bởi Deployment. Bởi cả 2 đều được quản lý bởi Deployment
```