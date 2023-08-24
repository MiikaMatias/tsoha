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
                }
            }
        }
    }
    
}
