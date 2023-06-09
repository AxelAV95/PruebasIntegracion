pipeline {
    agent any

    stages {
        stage('Test Python') {
            steps {
                bat '''
                    "C:/Users/AxelAV/AppData/Local/Programs/Python/Python311/python.exe" -m pytest sesion.py
                '''
            }
        }
        
         stage('Test git') {
            steps {
                bat '''
                    git status
                '''
            }
        }
 
    }
}
