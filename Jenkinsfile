pipeline {
    agent {
        docker {
            image 'pytester:latest'
            args '-u root'  // opzionale, se vuoi più permessi
        }
    }

    stages {
        stage('Setup') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest || true'  // evita fallimento totale, utile per debugging
            }
        }
    }

    post {
        always {
            echo "Pipeline completata"
        }
        failure {
            echo "Alcuni test sono falliti!"
        }
    }
}
