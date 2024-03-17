pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Configurar Python') {
            steps {
                tool 'Python 3.8'
            }
        }
        stage('Levantar contenedores y crear base de datos') {
            steps {
                sh 'docker-compose up -d'
                sh 'docker-compose exec -T web python manage.py createdb'
            }
        }
        stage('Ejecutar pruebas') {
            steps {
                sh 'docker-compose exec -T web bash -c "cd tests && coverage run -m unittest discover -s . && coverage report -m --fail-under=80"'
            }
        }
    }
}