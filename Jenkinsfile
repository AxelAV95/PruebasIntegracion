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
                    "C:/git-ftp-1.6.0/git-ftp.bat" push --syncroot . --user ftptest --passwd admin ftp://192.168.100.252/
                    echo "new content" >> index.txt
                    git add index.txt
                    git commit -m "Add new content"
                    git push --set-upstream origin testing
                    "C:/git-ftp-1.6.0/git-ftp.bat" push --syncroot . --user ftptest --passwd admin ftp://192.168.100.252/

                '''
            }
        }

    }
}
