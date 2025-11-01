# Practice-Flask-SQLAlchemy
Practica de SQLAlchemy con el modelo relacional de farmacia

## Requisitos
- Python 3.12+
- MySQL Server

## Dependencias
Las dependencias del proyecto están listadas en `requirements.txt`:
- Flask 3.0.3
- Flask-SQLAlchemy 3.1.1
- Flask-Marshmallow 1.2.1
- marshmallow-sqlalchemy 1.1.0
- PyMySQL 1.1.1
- cryptography 43.0.3

## Instalación

### 1. Crear y activar el entorno virtual

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Para ejecutar el API

### Opción 1: Ejecución local (sin Docker)
```bash
cd app
python run.py
```

### Opción 2: Ejecución con Docker (Recomendado)

#### Construir y ejecutar con Docker Compose
```bash
# Construir y levantar los contenedores
docker-compose up --build

# O en modo detached (en segundo plano)
docker-compose up -d --build
```

#### Detener los contenedores
```bash
docker-compose down
```

#### Ver logs
```bash
# Ver logs de todos los servicios
docker-compose logs

# Ver logs solo de la aplicación
docker-compose logs web

# Ver logs solo de la base de datos
docker-compose logs db
```

#### Reconstruir la aplicación después de cambios
```bash
docker-compose up --build web
```

## Estructura de Docker

- **Dockerfile**: Define la imagen de la aplicación Flask
- **docker-compose.yml**: Orquesta la aplicación Flask y MySQL
- **init.sql**: Script de inicialización de la base de datos (opcional)

## Variables de Entorno

La aplicación usa las siguientes variables de entorno para la conexión a la base de datos:

- `DB_HOST`: Host de la base de datos (default: localhost)
- `DB_PORT`: Puerto de MySQL (default: 3306)
- `DB_NAME`: Nombre de la base de datos (default: farmacia)
- `DB_USER`: Usuario de MySQL (default: root)
- `DB_PASSWORD`: Contraseña de MySQL (default: vacío)

## Acceso a la Aplicación

Una vez que los contenedores estén corriendo:
- API Flask: http://localhost:5000
- MySQL: localhost:3306