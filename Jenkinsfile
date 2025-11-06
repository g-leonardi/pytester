pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Assicuriamoci di avere Python e pip
                sh 'python3 --version'
                sh 'pip3 --version'

                // Installiamo le dipendenze
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Eseguiamo i test (ad esempio pytest)
                sh 'pytest'
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
