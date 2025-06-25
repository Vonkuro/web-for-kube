# web-for-kube

# Commands
## Namespace
```
kubectl create namespace prod 
kubectl create namespace dev
```
## image build
```
cd src
docker build -t web-for-kube .
```
## helm deployment
```
cd ../web-for-kube
helm install web-for-kube . -n dev -f values-dev.yaml
helm install web-for-kube . -n prod -f values-prod.yaml
```