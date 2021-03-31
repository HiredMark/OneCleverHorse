pipeline{
    environment {
        registry = "78afec35/onecleverhorse"
        registryCredential = '78afec35' 
        dockerImage = '' 
    }
    agent any
    stages{
        stage('Clean and Download'){
            steps{
                sh "rm -rf OneCleverHorse/"
                sh "git clone https://github.com/78afec35/OneCleverHorse"
            }
        }
    

        stage('Set Up Environment'){
            steps{
                sh "sudo sh ./startupscript.sh"

            }
        }
    
        stage('Build'){
            steps{
                sh "sudo docker-compose build"
            }
        }
        
        stage('Test'){
            steps{
                sh "sudo docker-compose up"
            }
        }
        
        stage('Naming Image') { 
            steps { 
                script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
            } 
        }
        
        stage('Pushing image') { 
            steps { 
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                } 
            }
        } 

        

        stage('Clean up'){
            steps{
                sh "sudo docker-compose down"
                sh "sudo docker image prune -f -a"
            }
        }
                
    }
}