bash build/build_postgres.sh
echo Built Postgres
bash build/build_imageboard.sh
echo Built Imageboard

bash deploy/deploy_postgres.sh
echo Deployed postgres
bash deploy/deploy_imageboard.sh
echo Deployed imageboard

docker ps