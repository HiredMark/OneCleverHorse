pipeline{
    agent any
    environment {
            app_version = "$BUILD_NUMBER"
            DATABASE_URI = credentials("DATABASE_URI")
            SECRET_KEY = credentials("SECRET_KEY")
            rollback = 'false'
        }
    stages{
        stage('Clean and Download'){
            steps{
                sh "sudo rm -rf OneCleverHorse/"
                sh "git clone https://github.com/78afec35/OneCleverHorse"
            }
        }
    

        stage('Set Up Environment'){
            steps{
                sh "sudo sh ./startupscript.sh"
                sh "docker image prune -f -a"

            }
        }
    
        stage('Run tests'){
            steps{
                sh "sudo sh ./tests.sh"

            }
        }
    
        stage('Build Image'){
                steps{
                  sh "docker-compose build"  
                }
            }
        
        stage('Push Image'){
                steps{
                    sh "docker-compose push"  
                }
            }
        stage('Test Deploy'){
            steps{
                sh "docker-compose up -d"
            }
        } 
        stage('Clean up'){
            steps{
                sh "docker-compose down"
                sh "docker image prune -f -a"
            }
        }
        stage('Ansible Config'){
            steps{
                sh "cd ansible && /home/jenkins/.local/bin/ansible-playbook -i inventory.yaml playbook.yaml"
            }
        }
        stage('Stack Deploy'){
            steps{
                sh "sudo sh ./stack_run.sh"
            }
        }
                
    }
}