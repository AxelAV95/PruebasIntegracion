pipeline {
	agent any
    	stages {

		stage('Actualizando repositorio local') {
            		/*	git status
                    			git add .
					git commit -m "Actualizando repositorio"*/
					
					steps {
                		 bat '''
                    		

                		'''
				
            		}
        	}
		
		stage('Pruebas Unitarias') {
            		steps {
                		echo "Ejecutando pruebas..."
				 bat '''
						 php ./phpunit.phar --bootstrap ./model/model.php ./test
                		'''
				
            		}
        	}
				

        	stage('Pruebas de Selenium') {
            		steps {
                		echo "Ejecutando pruebas..."
				 bat '''

                		'''
				
            		}
        	}

		
    }
    post {
        	always {
            		echo "Termino el test"
        	}
		success{
			
			echo "Enviando correo de caso exitoso"
			/*mail(to:'adriortiz0333@gmail.com',subject:'Testing - Integración continua',body:'Integracion continua ha superado las pruebas.');
			mail(to:'azofeifamelanysofia@gmail.com',subject:'Testing - Integración continua',body:'Integracion continua ha superado las pruebas.');*/

			echo "Aplicando Merge"
				/*git checkout main
                    		git merge Dev*/
                	bat '''
                    		

                	'''

			echo "Subiendo a FTP"

			
                	bat '''                    		

                	'''
			
						
		}
		   			
		failure{
			echo "Enviando correo de fallos"			
			/*mail(to:'adriortiz0333@gmail.com',subject:'Testing - Integración continua',body:'Integracion continua no ha superado las pruebas.');
			mail(to:'azofeifamelanysofia@gmail.com',subject:'Testing - Integración continua',body:'Integracion continua no ha superado las pruebas.');*/
						
		}
	}
	 
}
