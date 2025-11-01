# Comandos Útiles de Docker

## Gestión de Contenedores

### Iniciar los servicios
```bash
docker-compose up
```

### Iniciar en modo detached (segundo plano)
```bash
docker-compose up -d
```

### Reconstruir las imágenes
```bash
docker-compose up --build
```

### Detener los servicios
```bash
docker-compose down
```

### Detener y eliminar volúmenes (⚠️ Esto eliminará los datos de la BD)
```bash
docker-compose down -v
```

## Ver Estado y Logs

### Ver estado de los contenedores
```bash
docker-compose ps
```

### Ver logs de todos los servicios
```bash
docker-compose logs
```

### Ver logs en tiempo real
```bash
docker-compose logs -f
```

### Ver logs de un servicio específico
```bash
docker-compose logs web
docker-compose logs db
```

## Acceso a Contenedores

### Ejecutar comandos en el contenedor de la aplicación
```bash
docker-compose exec web bash
```

### Ejecutar comandos en el contenedor de MySQL
```bash
docker-compose exec db bash
```

### Conectar a MySQL desde la línea de comandos
```bash
docker-compose exec db mysql -u farmacia_user -pfarmacia_pass farmacia
```

### Conectar como root a MySQL
```bash
docker-compose exec db mysql -u root -prootpassword farmacia
```

## Gestión de Base de Datos

### Hacer backup de la base de datos
```bash
docker-compose exec db mysqldump -u root -prootpassword farmacia > backup.sql
```

### Restaurar backup
```bash
docker-compose exec -T db mysql -u root -prootpassword farmacia < backup.sql
```

### Ver tablas en la base de datos
```bash
docker-compose exec db mysql -u root -prootpassword -e "USE farmacia; SHOW TABLES;"
```

## Limpieza

### Eliminar contenedores detenidos
```bash
docker container prune
```

### Eliminar imágenes no usadas
```bash
docker image prune
```

### Eliminar volúmenes no usados
```bash
docker volume prune
```

### Limpieza completa del sistema Docker
```bash
docker system prune -a
```

## Desarrollo

### Reiniciar solo el servicio web
```bash
docker-compose restart web
```

### Reconstruir solo el servicio web
```bash
docker-compose up -d --no-deps --build web
```

### Ver variables de entorno del contenedor
```bash
docker-compose exec web env
```

## Troubleshooting

### Si el puerto 3306 ya está en uso
Edita `docker-compose.yml` y cambia el puerto:
```yaml
ports:
  - "3307:3306"  # Usar puerto 3307 en el host
```

### Si el puerto 5000 ya está en uso
Edita `docker-compose.yml` y cambia el puerto:
```yaml
ports:
  - "5001:5000"  # Usar puerto 5001 en el host
```

### Verificar que MySQL esté listo
```bash
docker-compose exec db mysqladmin ping -h localhost -u root -prootpassword
```

### Reiniciar desde cero
```bash
docker-compose down -v
docker-compose up --build
```
