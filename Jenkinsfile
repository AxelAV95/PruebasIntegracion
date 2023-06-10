pipeline {
	agent any
    	stages {

			stage('Actualizando repositorio local') {
						steps {
							/*git config --global user.email "adriortiz0333@gmail.com"
									git config --global user.name "adriortiz0333"*/
							bat '''
									

							'''				
						}
				}
			
			stage('Pruebas Unitarias') {
					steps {
						echo "Ejecutando pruebas..."
						bat '''

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
