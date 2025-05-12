pipeline {
  agent any 

  options{
        // Max number of build logs to keep and days to keep
        buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '5'))
        // Enable timestamp at each job in the pipeline
        timestamps()
    }

    environment{
        registry = 'duc8504/jenskins-demo' // Địa chỉ dockerhub
        registryCredential = 'dockerhub'      
    }

  stages {
    stage('Clone Code') {
      steps {
        git url: 'https://github.com/PhamTrinhDuc/jenkins-demo.git', branch: 'main'      
      }
    }

    stage('Install Dependencies') {
      agent {
        docker {
          image 'python:3.9' 
        }
      }
      steps {
        sh 'pip install -r app/requirements.txt'
      }
    }

    stage('Run Tests') {
      steps {
        sh 'pytest app/tests'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
            echo 'Building image for deployment..'
            dockerImage = docker.build registry + ":$BUILD_NUMBER" 
            echo 'Pushing image to dockerhub..'
            docker.withRegistry( '', registryCredential ) {
                dockerImage.push()
                dockerImage.push('latest')
            }
        }
      }
    }
  }
}