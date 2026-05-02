pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '''
                python -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install pytest==7.4.3
				pip install openpyxl==3.1.2
                '''
            }
        }

        stage('Run All Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest tests
                '''
            }
        }

    }

    post {
        always {
            echo 'Test execution completed'
        }
        success {
            echo 'Build Passed'
        }
        failure {
            echo 'Build Failed'
        }
    }
}
