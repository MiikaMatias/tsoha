pipeline {
    agent any

    environment {
        SSH_KEY_DEPLOYMENT_SERVER = credentials('ds-ssh-key-imageboard')
        ROOT_DIRECTORY = '${JENKINS_HOME}/jobs/image-board-pipeline/workspace/'
        ENV_PATH = "$ROOT_DIRECTORY/src/.env" 
    }


    stages {
        stage('Read .env file') {
            steps{
                script {
                    cat ENV_PATH
                    // Read the .env file and load its content into a map
                    def envFile = readFile(ENV_PATH)
                    def envMap = [:]
                    envFile.readLines().each { line ->
                        def (key, value) = line.tokenize('=')
                        envMap[key] = value
                    }

                    // Set the environment variables using withEnv
                    withEnv(envMap) {
                        echo "DB_HOST: ${env.DB_HOST}"
                        echo "DB_PORT: ${env.DB_PORT}"
                        echo "DB_USER: ${env.DB_USER}"
                        echo "DB_PASS: ${env.DB_PASS}"
                        
                        // You can now use these variables in your build steps
                        // For example, you can use them in a shell step
                        sh 'echo $DB_HOST'
                    }
            }
        }

        stage("build") {
            steps {
                    withAWS(credentials:, region:) {
                    script {
                        sh 'docker build -t $IMAGEBOARD_IMAGE_NAME -f Dockerfile.imageboard .'
                        sh 'docker tag $IMAGEBOARD_IMAGE_NAME:latest $IMAGE_TAG:$IMAGEBOARD_IMAGE_NAME'
                        sh 'docker push $IMAGE_TAG:$IMAGEBOARD_IMAGE_NAME'
            
                        sh 'docker build -t $IMAGEBOARD_IMAGE_NAME -f Dockerfile.imageboard .'
                        sh 'docker tag $IMAGEBOARD_IMAGE_NAME:latest $IMAGE_TAG:$IMAGEBOARD_IMAGE_NAME'
                        sh 'docker push $IMAGE_TAG:$IMAGEBOARD_IMAGE_NAME'
                    }
                    }
                }
            }   

        stage("test") {
            steps {
                sh 'echo Start test:'

                sh 'echo Tests completed!'
            }
        }

        stage("deploy") {
            steps {
                withAWS(credentials:, region:) {
                    script {
                    sh 'echo "echo Start deploy:"'

                    sh ('aws eks update-kubeconfig --name $EKS_CLUSTER_NAME --region $REGION')
                    sh 'kubectl apply -f'

                    sh 'echo Deployment completed!'
                    }
                }
            }
        }
    }
    
}   