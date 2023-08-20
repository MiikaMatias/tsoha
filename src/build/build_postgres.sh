source .env

docker stop $POSTGRES_CONTAINER_NAME
docker rmi $POSTGRES_CONTAINER_NAME
docker rm $POSTGRES_IMAGE_NAME

docker build -t $POSTGRES_IMAGE_NAME -f Dockerfile.postgres .


