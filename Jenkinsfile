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
    }
    post{
        always{
            echo 'This will always run'
        }
        success{
            echo "This will only run if successful"
        }
    }
}