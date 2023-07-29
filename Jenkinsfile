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
                sshPublisher(publishers: [sshPublisherDesc(configName: 'ubuntu@13.49.78.156', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'pwd', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '/')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true)])                
                sh 'echo Deployment completed!'
            }
        }
    }
    
}   