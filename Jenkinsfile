pipeline {
    agent any

    environment {
        SSH_KEY_DEPLOYMENT_SERVER = credentials('ds-shh-key')
    }

    stages {

        stage("build") {
            steps {
                sh '''
                    echo "Building imageboard...
                    echo "This is the directory of the secret file $SSH_KEY_DEPLOYMENT_SERVER"
                    echo "This is the content of the file `cat $SSH_KEY_DEPLOYMENT_SERVER`"
                '''
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