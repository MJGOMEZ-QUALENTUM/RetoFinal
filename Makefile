# Comando para iniciar el contenedor y la base de datos si se ha borrado antes o es la primera vez
inicio:
	docker-compose up -d 
	docker-compose exec web python manage.py

# Comando para ejecutar los tests y ver su cobertura
testear:
	docker-compose exec web bash -c 'cd tests && coverage run -m unittest discover -s . && coverage report -m --fail-under=80'

# Comando para detener el contendor, sin borrar la base de datos
parar:
	docker-compose down

# Comando para detener el contendor, borrando la base de datos, todos los contendores y todas las imágenes que se tenían antes
detener:
	docker-compose down --remove-orphans -v
	docker system prune -a --volumes --force

# Comando para reanudar el contenedor si no se borraron sus datos antes
reanudar:
	docker-compose up -d

# comentario de prueba

