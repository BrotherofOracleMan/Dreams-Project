/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'ruby:3.3.0-alpine3.19' } }
    stages {
        stage('build') {
            steps {
                sh 'ruby --version'
            }
        }
    }
}