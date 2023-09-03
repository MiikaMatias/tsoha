eval $(minikube docker-env)

kubectl delete all --all
docker build -t imageboard-app -f Dockerfile.imageboard .
docker build -t imageboard-db -f Dockerfile.postgres .
kubectl apply -f local_test_deployment.yml

minikube ip