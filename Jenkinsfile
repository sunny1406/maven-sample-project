def output = 'From Jenkins'
def x = '1010'
pipeline {
    agent {
        label 'slave-node'
    }

    stages {
        stage('checkout') {
            steps {
              git 'git@github.com:sunny1406/Maven_project_java.git'
              }
        }
        stage('Hello') {
            steps {
                echo "Hello World ${output}"
            }
        }
        stage('sample-test') {
            steps {
                echo "Print value ${x}"
            }
        }
        stage('validate') {
          steps {
            sh 'mvn validate'
            }
          }
        stage('compile') {
          steps {
            sh 'mvn compile'
          }
        }
        stage('test') {
          steps {
            sh 'mvn test'
          }
        }
        stage('package') {
          steps {
            sh 'mvn package'
          }
        }
        stage ('CleanUP') {
         cleanWs() 
        }
    }
}
