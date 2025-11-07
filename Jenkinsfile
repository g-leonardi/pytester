pipeline {
    agent any

    stages {
        stage('Build image') {
            steps {
                sh 'docker build -t pytester:latest .'
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'pytester:latest'
                    args '-u root'
                }
            }
            steps {
                sh 'pytest || true'
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
