pipeline {
    agent any
    stages {
        stage('Run Python Script') {
            steps {
                sh 'python -c "print(\'Hello World\')"'
            }
        }
    }
}