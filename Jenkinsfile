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
                    git branch
                    git checkout main
                    git branch
                    git checkout Dev
                    git branch
                '''
            }
        } 
    }
    
     post {
        	always {
            		echo "Termino el test"
        	}
		success{
		echo "Enviando correo exito"
			mail(to:'villalobos.axel@yahoo.es',subject:'Testing',body:'Termino exitosamente.');
			mail(to:'adriortiz0333@gmail.com',subject:'Testing',body:'Termino exitosamente.');
			mail(to:'azofeifamelanysofia@gmail.com',subject:'Testing',body:'Termino exitosamente.');
			
		  
			

			
		}
		failure{
			echo "Enviando correo error"
			mail(to:'villalobos.axel@yahoo.es, adriortiz0333@gmail.com, azofeifamelanysofia@gmail.com',subject:'Testing',body:'Fallo el test.');
			emailext body: 'Prueba de SAF2 integracion continua fallo', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Prueba de SAF2 integracion continua fallo'
            emailext (
                    subject: 'Alerta de actualizacion gitlab', 
                    mimeType: 'text/html', 
                    to: 'EMAIL',
                    recipientProviders: [[$class: 'CulpritsRecipientProvider'],[$class: 'RequesterRecipientProvider']], 
                    body: 'Integracion continua no ha superado las pruebas'
                )
		}
	}
}
