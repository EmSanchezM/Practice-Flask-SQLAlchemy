# Comandos cURL para probar la API Pharmacy

Base URL: `http://localhost:5000`

## Índice
- [Endpoint Raíz](#endpoint-raíz)
- [Users](#users)
- [Activities](#activities)
- [Customers](#customers)
- [Providers](#providers)
- [Products](#products)
- [Payments](#payments)
- [Inventory](#inventory)
- [Orders](#orders)
- [Payment Details](#payment-details)

---

## Endpoint Raíz

### GET / - Mensaje de bienvenida
```bash
curl -X GET http://localhost:5000/
```

---

## Users

### POST /users - Crear usuario
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Juan Pérez",
    "email": "juan.perez@example.com",
    "password": "password123"
  }'
```

### GET /users - Obtener todos los usuarios
```bash
curl -X GET http://localhost:5000/users
```

### GET /users/:id - Obtener un usuario específico
```bash
curl -X GET http://localhost:5000/users/1
```

### PUT /users/:id - Actualizar usuario
```bash
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Juan Pérez Actualizado",
    "email": "juan.updated@example.com",
    "password": "newpassword123"
  }'
```

### DELETE /users/:id - Eliminar usuario
```bash
curl -X DELETE http://localhost:5000/users/1
```

---

## Activities

### POST /activities - Crear actividad
```bash
curl -X POST http://localhost:5000/activities \
  -H "Content-Type: application/json" \
  -d '{
    "activity": "Usuario creado y configurado",
    "user_id": 1
  }'
```

### GET /activities - Obtener todas las actividades
```bash
curl -X GET http://localhost:5000/activities
```

### GET /activities/:id - Obtener una actividad específica
```bash
curl -X GET http://localhost:5000/activities/1
```

### PUT /activities/:id - Actualizar actividad
```bash
curl -X PUT http://localhost:5000/activities/1 \
  -H "Content-Type: application/json" \
  -d '{
    "activity": "Usuario actualizado correctamente",
    "user_id": 1
  }'
```

### DELETE /activities/:id - Eliminar actividad
```bash
curl -X DELETE http://localhost:5000/activities/1
```

---

## Customers

### POST /customers - Crear cliente
```bash
curl -X POST http://localhost:5000/customers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Farmacia Central",
    "address": "Calle Principal 123",
    "contact": "+34 900 123 456",
    "type_custom": "regular"
  }'
```

### GET /customers - Obtener todos los clientes
```bash
curl -X GET http://localhost:5000/customers
```

### GET /customers/:id - Obtener un cliente específico
```bash
curl -X GET http://localhost:5000/customers/1
```

### PUT /customers/:id - Actualizar cliente
```bash
curl -X PUT http://localhost:5000/customers/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Farmacia Central Premium",
    "address": "Calle Principal 123, Local A",
    "contact": "+34 900 123 999",
    "type_custom": "premium"
  }'
```

### DELETE /customers/:id - Eliminar cliente
```bash
curl -X DELETE http://localhost:5000/customers/1
```

---

## Providers

### POST /providers - Crear proveedor
```bash
curl -X POST http://localhost:5000/providers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laboratorios ABC",
    "prov_license": "LIC-12345-2024",
    "address": "Polígono Industrial, Nave 5"
  }'
```

### GET /providers - Obtener todos los proveedores
```bash
curl -X GET http://localhost:5000/providers
```

### GET /providers/:id - Obtener un proveedor específico
```bash
curl -X GET http://localhost:5000/providers/1
```

### PUT /providers/:id - Actualizar proveedor
**Nota:** Este endpoint tiene un bug en el código (falta el método HTTP en la ruta)
```bash
curl -X PUT http://localhost:5000/providers/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laboratorios ABC SA",
    "prov_license": "LIC-12345-2025",
    "address": "Polígono Industrial, Nave 5-6"
  }'
```

### DELETE /providers/:id - Eliminar proveedor
**Nota:** Este endpoint tiene un bug en el código (falta el método HTTP en la ruta)
```bash
curl -X DELETE http://localhost:5000/providers/1
```

---

## Products

### POST /products - Crear producto
**NOTA:** El campo `unit` debe ser un número entero (Integer), no texto.
```bash
curl -X POST http://localhost:5000/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Paracetamol 500mg",
    "unit": 100,
    "description": "Analgésico y antipirético",
    "provider_id": 1
  }'
```

### GET /products - Obtener todos los productos
```bash
curl -X GET http://localhost:5000/products
```

### GET /products/:id - Obtener un producto específico
```bash
curl -X GET http://localhost:5000/products/1
```

### PUT /products/:id - Actualizar producto
```bash
curl -X PUT http://localhost:5000/products/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Paracetamol 500mg (Genérico)",
    "unit": 150,
    "description": "Analgésico y antipirético - versión genérica",
    "provider_id": 1
  }'
```

### DELETE /products/:id - Eliminar producto
```bash
curl -X DELETE http://localhost:5000/products/1
```

---

## Payments

### POST /payments - Crear método de pago
```bash
curl -X POST http://localhost:5000/payments \
  -H "Content-Type: application/json" \
  -d '{
    "pay_mode": "Tarjeta de crédito"
  }'
```

### GET /payments - Obtener todos los métodos de pago
```bash
curl -X GET http://localhost:5000/payments
```

### GET /payments/:id - Obtener un método de pago específico
```bash
curl -X GET http://localhost:5000/payments/1
```

### PUT /payments/:id - Actualizar método de pago
```bash
curl -X PUT http://localhost:5000/payments/1 \
  -H "Content-Type: application/json" \
  -d '{
    "pay_mode": "Transferencia bancaria"
  }'
```

### DELETE /payments/:id - Eliminar método de pago
```bash
curl -X DELETE http://localhost:5000/payments/1
```

---

## Inventory

### POST /inventory - Crear inventario
```bash
curl -X POST http://localhost:5000/inventory \
  -H "Content-Type: application/json" \
  -d '{
    "cost": 5.50,
    "price": 8.99,
    "unit": 100,
    "product_id": 1
  }'
```

### GET /inventory - Obtener todo el inventario
```bash
curl -X GET http://localhost:5000/inventory
```

### GET /inventory/:id - Obtener un inventario específico
```bash
curl -X GET http://localhost:5000/inventory/1
```

### PUT /inventory/:id - Actualizar inventario
```bash
curl -X PUT http://localhost:5000/inventory/1 \
  -H "Content-Type: application/json" \
  -d '{
    "cost": 5.00,
    "price": 7.99,
    "unit": 150,
    "product_id": 1
  }'
```

### DELETE /inventory/:id - Eliminar inventario
**Nota:** Este endpoint tiene un bug en el código (typo: `ds.session` en lugar de `db.session`)
```bash
curl -X DELETE http://localhost:5000/inventory/1
```

---

## Orders

### POST /orders - Crear orden
```bash
curl -X POST http://localhost:5000/orders \
  -H "Content-Type: application/json" \
  -d '{
    "paymentMode": "Tarjeta de crédito",
    "comment": "Pedido urgente",
    "customer_id": 1,
    "user_id": 1
  }'
```

### GET /orders - Obtener todas las órdenes
```bash
curl -X GET http://localhost:5000/orders
```

### GET /orders/:id - Obtener una orden específica
```bash
curl -X GET http://localhost:5000/orders/1
```

### PUT /orders/:id - Actualizar orden
```bash
curl -X PUT http://localhost:5000/orders/1 \
  -H "Content-Type: application/json" \
  -d '{
    "paymentMode": "Efectivo",
    "comment": "Pedido procesado",
    "customer_id": 1,
    "user_id": 1
  }'
```

### DELETE /orders/:id - Eliminar orden
```bash
curl -X DELETE http://localhost:5000/orders/1
```

---

## Payment Details

### POST /payDetails - Crear detalle de pago
```bash
curl -X POST http://localhost:5000/payDetails \
  -H "Content-Type: application/json" \
  -d '{
    "quantity_ordered": 10,
    "price": 8.99,
    "order_id": 1,
    "product_id": 1
  }'
```

### GET /payDetails - Obtener todos los detalles de pago
```bash
curl -X GET http://localhost:5000/payDetails
```

### GET /payDetails/:id - Obtener un detalle de pago específico
```bash
curl -X GET http://localhost:5000/payDetails/1
```

### PUT /payDetails/:id - Actualizar detalle de pago
```bash
curl -X PUT http://localhost:5000/payDetails/1 \
  -H "Content-Type: application/json" \
  -d '{
    "quantity_ordered": 15,
    "price": 7.99,
    "order_id": 1,
    "product_id": 1
  }'
```

### DELETE /payDetails/:id - Eliminar detalle de pago
```bash
curl -X DELETE http://localhost:5000/payDetails/1
```

---

## Bugs Detectados

Durante la creación de los tests, se identificaron los siguientes problemas en el código:

1. **Endpoints de Providers (UPDATE y DELETE)**: Faltan los métodos HTTP en las decoraciones
   - Línea ~90: `@app.route('/providers/<id>')` debería ser `@app.route('/providers/<id>', methods=['PUT'])`
   - Línea ~103: `@app.route('/providers/<id>')` debería ser `@app.route('/providers/<id>', methods=['DELETE'])`

2. **Endpoint DELETE /inventory/:id**: Typo en el código
   - Línea ~450: `ds.session.commit()` debería ser `db.session.commit()`

3. **Endpoint PUT /orders/:id**: Typo en el nombre del campo
   - Línea ~223: `order.commet = comment` debería ser `order.comment = comment`
