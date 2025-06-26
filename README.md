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
minikube image load web-for-kube
cd ../web-for-kube
helm install web-for-kube . -n dev -f values-dev.yaml
helm install web-for-kube . -n prod -f values-prod.yaml
minikube service web-for-kube -n dev --url
minikube service web-for-kube -n prod --url
```

## helm uninstall
```
helm uninstall web-for-kube -n dev
helm uninstall web-for-kube -n prod
```

## helm supervisor
```
kubectl get all -n dev
kubectl get all -n prod

kubectl get events -n dev --sort-by=.lastTimestamp
kubectl get events -n prod --sort-by=.lastTimestamp
```