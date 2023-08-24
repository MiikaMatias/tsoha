pipeline {
    agent any

    environment {
        SSH_KEY_DEPLOYMENT_SERVER = credentials('ds-ssh-key-imageboard')
        ROOT_DIRECTORY = '${JENKINS_HOME}/jobs/image-board-pipeline/workspace'
        ENV_PATH = "$ROOT_DIRECTORY/src/.env" 
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: 'master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/MiikaMatias/tsoha.git']]])
                }
            }
        }
        stage('Read Files') {
            steps {
                script {
                    def fileContents = readFile('/src/.env')
                    echo "Contents of file.txt: ${fileContents}"
                }
            }
        }

    }
}
