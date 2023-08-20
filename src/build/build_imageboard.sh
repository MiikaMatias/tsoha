source .env

docker stop $IMAGEBOARD_CONTAINER_NAME
docker rmi $IMAGEBOARD_CONTAINER_NAME
docker rm $IMAGEBOARD_IMAGE_NAME

docker build -t $IMAGEBOARD_IMAGE_NAME -f Dockerfile.imageboard .

