
from routes import *

if __name__ == '__main__':
    # Crear tablas si no existen
    with app.app_context():
        db.create_all()
    
    # Ejecutar la aplicación en todas las interfaces (0.0.0.0)
    app.run(host='0.0.0.0', port=5000, debug=True)


