pipeline {
   agent {  
       docker { image 'node:9-alpine' }
    }
    stages {
       stage('#1 Git') {
            steps {
                git 'https://github.com/brunohafonso95/jenkins-postman-test.git'
            }  
       }
       stage('#2 install tools') {
           steps {
               sh 'npm i -g newman'
               sh 'npm install -g newman-reporter-html'
           }
       }
       stage('#3 start the service') {
           steps {
               sh 'python manage.py runserver'
           }
       }
       stage('#4 run tests') {
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