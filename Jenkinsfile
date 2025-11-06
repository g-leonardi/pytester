pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh '''
                    apt-get update && apt-get install -y python3-venv

                    python3 --version
                    pip3 --version

                    # Creiamo un virtual environment
                    python3 -m venv venv
                    . venv/bin/activate

                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline completata'
        }
        success {
            echo 'Tutti i test sono passati!'
        }
        failure {
            echo 'Alcuni test sono falliti!'
        }
    }
}
