pipeline {
   agent any
    stages {
       stage('#1 Git') {
            steps {
                git 'https://github.com/brunohafonso95/jenkins-postman-test.git'
            }  
       }
       stage('#2 install tools') {
           agent {
               docker { image 'tarampampam/node:alpine' }
           }
           steps {
                sh 'npm config set proxy http://proxylatam.indra.es:8080'
                sh 'npm config set https-proxy http://proxylatam.indra.es:8080'
                sh 'npm config set http-proxy http://proxylatam.indra.es:8080'
                sh 'npm i -g newman'
                sh 'npm install -g newman-reporter-html'
           }
       }
       stage('#3 start the service') {
           agent {
               docker { image 'python:3.7-alpine' }
           }
           steps {
               sh 'pip --proxy http://proxylatam.indra.es:8080 install -r requeriments.txt'
               sh 'python manage.py runserver'
           }
       }
       stage('#4 run tests') {
           agent {
               docker { image 'tarampampam/node:alpine' }
           }
           steps {
               sh 'rm -r ./newman'
               sh 'newman run postman.json -r junit,html'
           }
       }
    }
    post {
        always {
            junit 'newman/**/*.xml'
            script {
                zip archive: true, dir: 'newman', glob: '', zipFile: 'report-files.zip'
            }
        }
    }
}