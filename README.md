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
```bash
cd app
python run.py
```