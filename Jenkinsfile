pipeline {
    agent any

    environment {
        SSH_KEY_DEPLOYMENT_SERVER = credentials('ds-ssh-key-imageboard')
        ROOT_DIRECTORY = '${JENKINS_HOME}/jobs/image-board-pipeline/workspace/'
    }

    stages {
        stage("build") {
            steps {
                sh 'echo Start build:'
                sh 'env | sort'

                sh 'echo Build completed!'
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
                sh 'echo "echo Start deploy:"'
                sh 'ssh-copy-id -i $SSH_KEY_DEPLOYMENT_SERVER ubuntu@13.49.78.156'
                sh 'rsync $ROOT_DIRECTORY ubuntu@13.49.78.156:~/app'
                sh 'echo Deployment completed!'
            }
        }
    }
    
}   