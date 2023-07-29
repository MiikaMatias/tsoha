pipeline {
    agent any

    environment {
        SSH_KEY_DEPLOYMENT_SERVER = credentials('ds-shh-key')
    }

    stages {

        stage("build") {
            steps {
                echo "Start build..."
                echo "${SSH_KEY_DEPLOYMENT_SERVER}"
            }
        }

        stage("test") {
            steps {
                echo "Testing image-board"
            }
        }

        stage("deploy") {
            steps {
                echo "Deploying image-board"
            }
        }
    }
    
}   