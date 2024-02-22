/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    stages {
        stage('Test') {
            steps {
               sh 'echo "Fail!"; exit 1'
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