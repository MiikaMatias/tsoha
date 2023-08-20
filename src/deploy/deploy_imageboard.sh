source .env

docker run --name $IMAGEBOARD_CONTAINER_NAME -d $IMAGEBOARD_IMAGE_NAME 

docker logs $IMAGEBOARD_CONTAINER_NAME

# gunicorn -b 0.0.0.0:5000 app:app