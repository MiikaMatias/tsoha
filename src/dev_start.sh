source .env
eval $(minikube docker-env)

bash build/build_postgres.sh
echo Built $POSTGRES_CONTAINER_NAME
bash build/build_imageboard.sh
echo Built $POSTGRES_IMAGE_NAME

docker save $POSTGRES_CONTAINER_NAME | (eval $(minikube -p minikube docker-env) && docker load)
docker save $POSTGRES_IMAGE_NAME | (eval $(minikube -p minikube docker-env) && docker load)
echo Saved $POSTGRES_IMAGE_NAME $POSTGRES_CONTAINER_NAME to minikube

kubectl delete all --all

kubectl apply -f persistent-volume.yml
kubectl apply -f imageboard-deployment.yml
echo Deployed $POSTGRES_CONTAINER_NAME
echo Deployed $POSTGRES_IMAGE_NAME