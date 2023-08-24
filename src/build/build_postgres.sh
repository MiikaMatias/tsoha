PARENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/.."
ENV_FILE="$PARENT_DIR/.env"

if [[ -f "$ENV_FILE" ]]; then
  source "$ENV_FILE"
else
  echo "ERROR: .env file not found in the parent directory."
  exit 1
fi


docker stop $DATABASE_CONTAINER_NAME
docker rm $DATABASE_CONTAINER_NAME
docker rmi $DATABASE_IMAGE_NAME

docker build -t $DATABASE_IMAGE_NAME -f Dockerfile.postgres .

docker tag $DATABASE_IMAGE_NAME:latest $IMAGE_TAG:$DATABASE_IMAGE_NAME
docker push $IMAGE_TAG:$DATABASE_IMAGE_NAME

