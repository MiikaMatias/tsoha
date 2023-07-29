pipeline {
    agent any

    environment {
        SSH_KEY_DEPLOYMENT_SERVER = 'var'
    }

    stages {
        stage("build") {
            steps {
                sh 'echo env | sort'
                sh 'echo $SSH_KEY_DEPLOYMENT_SERVER'
                }
            }   
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