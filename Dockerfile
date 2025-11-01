# Usar imagen oficial de Python
FROM python:3.12-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requisitos
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app/ ./app/

# Exponer el puerto en el que correrá Flask
EXPOSE 5000

# Variables de entorno por defecto
ENV FLASK_APP=app/run.py
ENV FLASK_ENV=development

# Comando para ejecutar la aplicación
CMD ["python", "app/run.py"]
