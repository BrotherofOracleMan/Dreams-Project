/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }

    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE = 'POSTGRES'
    }
    stages {
        stage('Build') {
            steps {
               echo "Database engine is ${DB_ENGINE}"
               echo "DISABLE_AUTH is ${DISABLE_AUTH}"
               sh 'printenv'
            }
        }

        stage('Test'){
            steps{
                sh './gradlew check'
            }
        }

    }
    post{
        always{
            junit 'build/reports/**/*.xml'
        }
        success{
            echo "This will only run if successful"
        }
    }
}