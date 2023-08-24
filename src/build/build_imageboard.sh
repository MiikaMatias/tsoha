PARENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."
ENV_FILE="$PARENT_DIR/.env"

if [[ -f "$ENV_FILE" ]]; then
  source "$ENV_FILE"
else
  echo "ERROR: .env file not found in the parent directory."
  exit 1
fi

docker stop $IMAGEBOARD_CONTAINER_NAME
docker rm $IMAGEBOARD_CONTAINER_NAME
docker rmi $IMAGEBOARD_IMAGE_NAME

docker build -t $IMAGEBOARD_IMAGE_NAME -f Dockerfile.imageboard .

docker tag $IMAGEBOARD_IMAGE_NAME:latest $IMAGE_TAG:$IMAGEBOARD_IMAGE_NAME
docker push $IMAGE_TAG:$IMAGEBOARD_IMAGE_NAME

