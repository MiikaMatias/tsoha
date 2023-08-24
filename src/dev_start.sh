source .env

sudo aws --region $REGION ecr get-login-password | docker login --username AWS --password-stdin $IMAGE_TAG
sudo kubectl create secret generic $ENVIRONMENT_NAME --from-env-file=.env

bash build/build_postgres.sh
echo Built $POSTGRES_CONTAINER_NAME
bash build/build_imageboard.sh
echo Built $POSTGRES_IMAGE_NAME

sudo kubectl delete all --all

bash deploy/deploy.sh
sudo kubectl apply -f deployment.yml
echo Deployed $POSTGRES_CONTAINER_NAME
echo Deployed $POSTGRES_IMAGE_NAME