# Message board project
[Production](http://ec2-16-171-11-122.eu-north-1.compute.amazonaws.com/)

[Architecture](https://github.com/MiikaMatias/tsoha/blob/main/docs/Architecture.md)
## Introduction
This project will contain a flask coded image-based messageboard application that will be deployed to a kubernetes cluster. It will implement a rudimentary CI/CD pipeline using Jenkins. The project will be deployed through AWS.  

## Requirements
There are certain primary requirements in the project:

1) The project will contain a method of user authentication using Kubernetes secrets. Each user of the message board has their own passwords and message history. 
2) The project will contain two containers. The primary application with all of the front-end, and a postgreSQL database. These will be deployed together as a multi-container deployment into a production server.
3) Each user will be able to make threads into the main page of the application. Each thread contains a chronological sequence of messages with the username, timestamp and images, if applicable. Both messages and threads can be removed by the users who created them, or by possible administrators.
4) Each user will also be able to access user information and statistics.
5) Messages will have an upvote and a downvote functionality. Threads may be sorted based on upvotes and activity.
6) The application will track traffic to it

The key learning goal of the project is to be able to set up a holistic web application. While familliar with all of these technologies, I've never implemented a holistic project based on them. Hence, this is somewhat of an integrative exercise. 

## Jenkins Pipeline
Pipeline will have the traditional segments of "build", "test" and "deploy". It will be directly attached to the Github repository, and will deploy the product into the production server. If you'd like to access Jenkins, ask me and give a good reason. 

## Kubernetes cluster
The cluster will contain a singular pod with two containers, one being the application front-end and the other one being the postgreSQL database.

## Service providers
All services will be run in AWS, paid from my own pocket.

## Concerning review
If course review using all of these external dependencies does not work, I can make one version using the CI/CD deployment system and one without it for review.


# How to run locally

1) Create a python virtual environment and install the requirements.txt files there

2) Make sure your postgresql server is running

3) Initialize database with sql schema

'psql  -U [username] -d [db-name] -f imageboard-db.sql'

replace DATABASE_URL in the app.py and SECRET_KEY in .env with your personal values
