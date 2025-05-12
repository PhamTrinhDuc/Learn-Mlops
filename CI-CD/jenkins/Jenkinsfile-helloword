pipeline {
    // Any available agent ip:port or an docker image
    agent any

    stages {
        stage('Test') {
            // Only run when it has some changes in a file
            // when { changeset "main.py" }

            // Only run when it has some changes in a branch
            // when { branch 'master' }

            steps {
                echo 'Testing something..'
            }
        }
        stage('Build') {
            steps {
                echo 'Building something..'

            }
        }
        stage('Deploy') {
            steps {
                input "Approve?"
                // A box will be displayed to show whether to proceed 
                // with the deployment
                // input 'Do you approve deployment?'
                echo 'Deploying something..'
            }
        }
    }
}