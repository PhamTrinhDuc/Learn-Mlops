### Install Terraform for Ubuntu 22.04
https://computingforgeeks.com/how-to-install-terraform-on-ubuntu/

## How-to Guide
Authenticate with GCP
```shell
gcloud auth application-default login
```
Switch to diffrent projects
```shell
gcloud config set project
```

## Provision a new cluster
```shell
terraform init
terraform plan
terraform apply
```