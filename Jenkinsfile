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
                stash name: 'node dependencies', useDefaultExcludes: false
           }
       }
       stage('#3 start the service') {
           agent {
               docker { image 'python:3.7-alpine' }
           }
           steps {
               sh 'pip --proxy http://proxylatam.indra.es:8080 install -r requeriments.txt'
               stash name: 'python dependencies', useDefaultExcludes: false
           }
       }
       stage('#4 run tests') {
           agent {
               docker { image 'mikeallanson/python3-node:0.0.8' }
           }
           steps {
                unstash 'node dependencies'
                unstash 'python dependencies'
                sh 'rm -r ./newman'
                sh 'python manage.py runserver'
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
}W@