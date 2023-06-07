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

        stage('Deploy to FTP') {
            steps {
                bat '''
                    git config --global user.email "villalobos.axel@yahoo.es"
                    git config --global user.name "AxelAV95"
                    git checkout -b testing
                    git config git-ftp.url "ftp://192.168.100.252"
                    git config git-ftp.user "ftptest"
                    git config git-ftp.password "admin"
                    git ftp push
                    git ftp init
                    echo "new content" >> index.txt
                    git commit index.txt -m "Add new content"
                    git push
                    git ftp push
                '''
            }
        }
    }
}
