# How-to Guide

## Smoke test our image locally

```bash
docker build -t foo . && docker run -p 30001:30000 foo
```

Open any browser and access this address `http://localhost:30001/docs` and play around with the Swagger UI.

Another way to play with your API is by using the library `requests`. Open a new terminal outside the dev container and run the following commands:

```bash
pip install -r .devcontainer/requirements_dev.txt
cd examples/
python predict.py
```

## Prepare for deployment on GCP

### Set up Jenkins

Create a new VM

```shell
cd iac/ansible
ansible-playbook create_compute_instance.yaml
```

Deploy our custom Jenkins (which use the custom image from the folder `custom_images/jenkins`) as follows:
  - Update the IP of the newly created instance to the `inventory` file
  - Run the following commands:
    ```shell
    cd deploy_jenkins
    ansible-playbook -i ../inventory deploy_jenkins.yml
    ```

### Install k8s plugin on Jenkins

Please install the `Kubernetes` plugin and set up a connection to GKE as guidance on the lesson.

Don't forget to grant permissions to the service account which is trying to connect to our cluster by the following command:

```shell
kubectl create ns model-serving
kubectl create clusterrolebinding model-serving-admin-binding \
  --clusterrole=admin \
  --serviceaccount=model-serving:default \
  --namespace=model-serving

kubectl create clusterrolebinding anonymous-admin-binding \
  --clusterrole=admin \
  --user=system:anonymous \
  --namespace=model-serving
```

### Set up pre-commit

- Run the following command to ask `pre-commit` to run on every commit
  ```shell
  pre-commit install
  ```
- You can also ask `pre-commit` to run on all files now by running
  ```shell
  pre-commit run --all-files
  ```

### YAMLlint

Verify all of your YAML files by running the following command:

  ```shell
  yamllint .
  ```
