pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from Git repository...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Setting up Python Environment and resolving path constraints...'
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip --user
                pip install pytest
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running pytest suite in verbose mode...'
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
