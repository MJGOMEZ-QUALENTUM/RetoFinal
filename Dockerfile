# Usa una imagen de Python oficial como base
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 en el contenedor
EXPOSE 5000

# Define la variable de entorno FLASK_ENV por defecto como desarrollo
ENV FLASK_ENV=development

# CMD especifica el comando que se ejecutará al iniciar el contenedor
CMD ["python", "run.py"]

