/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }

    environment {
        DISABLE_AUTH = 'true'
        DB_ENGINE = 'POSTGRES'
    }

    options{
        skipStagesAfterUnstable()
    }

    stages {
        stage('Build') {
            steps{
                echo 'Building'
            }
        }

        stage('Test'){
            steps{
                echo 'Testing'
            }
        }

        stage('Deploy'){
            steps{
                echo 'Deploying'
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