pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from SCM...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Setting up Python Environment and installing requirements...'
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install pytest
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests in verbose mode...'
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat '''
                    call venv\\Scripts\\activate
                    pytest -v
                    '''
                }
            }
        }
    }
}
