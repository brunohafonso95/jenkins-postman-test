pipeline {
   agent any
    stages {
       stage('#1 Git') {
            steps {
                git 'https://github.com/brunohafonso95/jenkins-postman-test.git'
            }  
       }
      stage('#2 run tests') {
           agent {
               docker { image 'brunohafonso95/newman-django:1.0' }
           }
           steps {
                sh 'rm -r ./newman'
                sh 'python manage.py runserver'
                sh 'newman run postman.json -r junit,html'
           }
       }
    }
    post {
        always {
            junit 'newman/**/*.xml'
            publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: './newman', reportFiles: '*.html', reportName: 'Test Reports', reportTitles: ''])
            script {
                zip archive: true, dir: 'newman', glob: '', zipFile: 'report-files.zip'
            }
        }
    }
}