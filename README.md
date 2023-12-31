# Message board project
[Production](http://ec2-13-48-177-96.eu-north-1.compute.amazonaws.com:30010/threads)

[Architecture](https://github.com/MiikaMatias/tsoha/blob/main/docs/Architecture.md)
## Introduction
This project contains a flask coded image-based messageboard application that is deployed to a kubernetes cluster. The project is deployed through AWS.

## Features
The primary features of the project:

1) User profiles: Users may register into the forum. Passwords are stored in an encrypted format. 
2) The project contains two containers. The primary application with all of the site logic, and a postgreSQL database. They will be running on their own deployments in the production server. The deployments are configured based on a .env file and a dev_start.sh script based rudimentary pipeline. 
3) An user is able to make threads into the main page of the application. Each thread contains a chronological sequence of messages with the username, timestamp and png based images. Adding images is mandatory. Both messages and threads can be removed by the users who created them.
4) Each user will also be able to access to a user landing zone with all threads that they've made.
5) Threads are sorted based on the amount of messages in them.

The key learning goal of the project is to be able to set up a holistic web application. While familliar with all of these technologies, I've never implemented a holistic project based on them. Hence, this is somewhat of an integrative exercise. 

## Jenkins Pipeline
Pipeline will have the traditional segments of "build", "test" and "deploy". It will be directly attached to the Github repository, and will deploy the product into the production server. If you'd like to access Jenkins, ask me and give a good reason. 

Pipeline was not used after a while, due to it being easier to test the project in a local minikube cluster. 

## Kubernetes cluster
The EKS cluster runs on an AWS server, and contains two deployments running the python code and the postgres database respectively

# How to run locally (if production is down)

This is a secondary method of testing the project if the link to the production environment fails

1) [Install minikube and all pre-requisites for running it](https://minikube.sigs.k8s.io/docs/start/)
2) Start your minikube cluster
3) CD to /src and run 'bash redeploy.sh'; uses local_test_deployment.yml which contains sample values and is NOT meant to be deployed online
4) Use the ip address provided at the end of the redeploy script and go to ´http://[minikube-ip]:30010´
5) you should now be able to access the project

## Alternative for kubernetes
1) Set up your own postgres database
2) apply imageboard.sql schema to it
3) make database url connect to it and comment out redundancies
![image](https://github.com/MiikaMatias/tsoha/assets/100348027/5a6689b0-bcea-4e03-b59c-5647a81acbff)
4) create a venv in python and install requirements.txt
5) run python3 -m flask run in src
