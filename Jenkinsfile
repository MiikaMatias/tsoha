pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = credentials('AWS_DEFAULT_REGION')
        AWS_ACCOUNT_ID = credentials('AWS_ACCOUNT_ID')
        ECR_REGISTRY_URL = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
        DOCKER_IMAGE_NAME = 'imageboard-app'
        DOCKER_IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/MiikaMatias/tsoha.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def customImage = docker.build("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}", "-f /src/Dockerfile.imageboard .")
                }
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                script {
                    withAWS(region: AWS_DEFAULT_REGION, credentials: 'your-aws-credentials-id') {
                        sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY_URL}"
                        docker.withRegistry(ECR_REGISTRY_URL, 'ecr:us-east-1:your-aws-credentials-id') {
                            def customImage = docker.image("${DOCKER_IMAGE_NAME}:${DOCKER_IMAGE_TAG}")
                            customImage.push()
                        }
                    }
                }
            }
        }
    }
}
