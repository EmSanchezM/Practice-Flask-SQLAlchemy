#!/bin/bash

# Script para probar todos los endpoints de la API Pharmacy
# Asegúrate de que la aplicación esté corriendo en http://localhost:5000

BASE_URL="http://localhost:5000"

echo "=========================================="
echo "Probando API Pharmacy"
echo "=========================================="
echo ""

# Test 1: Endpoint raíz
echo "1. Probando endpoint raíz (GET /)..."
curl -X GET "${BASE_URL}/"
echo -e "\n"

# ==================== USERS ====================
echo "=========================================="
echo "PROBANDO ENDPOINTS DE USERS"
echo "=========================================="
echo ""

# Test 2: Crear usuario
echo "2. Creando un nuevo usuario (POST /users)..."
USER_RESPONSE=$(curl -s -X POST "${BASE_URL}/users" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Juan Pérez",
    "email": "juan.perez@example.com",
    "password": "password123"
  }')
echo "$USER_RESPONSE"
USER_ID=$(echo $USER_RESPONSE | grep -o '"id":[0-9]*' | grep -o '[0-9]*' | head -1)
echo -e "\n"

# Test 3: Obtener todos los usuarios
echo "3. Obteniendo todos los usuarios (GET /users)..."
curl -X GET "${BASE_URL}/users"
echo -e "\n"

# Test 4: Obtener un usuario específico
echo "4. Obteniendo usuario con ID ${USER_ID} (GET /users/${USER_ID})..."
curl -X GET "${BASE_URL}/users/${USER_ID}"
echo -e "\n"

# Test 5: Actualizar usuario
echo "5. Actualizando usuario con ID ${USER_ID} (PUT /users/${USER_ID})..."
curl -X PUT "${BASE_URL}/users/${USER_ID}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Juan Pérez Actualizado",
    "email": "juan.perez.updated@example.com",
    "password": "newpassword123"
  }'
echo -e "\n"

# ==================== ACTIVITIES ====================
echo "=========================================="
echo "PROBANDO ENDPOINTS DE ACTIVITIES"
echo "=========================================="
echo ""

# Test 6: Crear actividad
echo "6. Creando una nueva actividad (POST /activities)..."
ACTIVITY_RESPONSE=$(curl -s -X POST "${BASE_URL}/activities" \
  -H "Content-Type: application/json" \
  -d "{
    \"activity\": \"Usuario creado y configurado\",
    \"user_id\": ${USER_ID}
  }")
echo "$ACTIVITY_RESPONSE"
ACTIVITY_ID=$(echo $ACTIVITY_RESPONSE | grep -o '"id":[0-9]*' | grep -o '[0-9]*' | head -1)
echo -e "\n"

# Test 7: Obtener todas las actividades
echo "7. Obteniendo todas las actividades (GET /activities)..."
curl -X GET "${BASE_URL}/activities"
echo -e "\n"

# Test 8: Obtener una actividad específica
echo "8. Obteniendo actividad con ID ${ACTIVITY_ID} (GET /activities/${ACTIVITY_ID})..."
curl -X GET "${BASE_URL}/activities/${ACTIVITY_ID}"
echo -e "\n"

# Test 9: Actualizar actividad
echo "9. Actualizando actividad con ID ${ACTIVITY_ID} (PUT /activities/${ACTIVITY_ID})..."
curl -X PUT "${BASE_URL}/activities/${ACTIVITY_ID}" \
  -H "Content-Type: application/json" \
  -d "{
    \"activity\": \"Usuario actualizado correctamente\",
    \"user_id\": ${USER_ID}
  }"
echo -e "\n"

# ==================== CUSTOMERS ====================
echo "=========================================="
echo "PROBANDO ENDPOINTS DE CUSTOMERS"
echo "=========================================="
echo ""

# Test 10: Crear cliente
echo "10. Creando un nuevo cliente (POST /customers)..."
CUSTOMER_RESPONSE=$(curl -s -X POST "${BASE_URL}/customers" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Farmacia Central",
    "address": "Calle Principal 123",
    "contact": "+34 900 123 456",
    "type_custom": "regular"
  }')
echo "$CUSTOMER_RESPONSE"
CUSTOMER_ID=$(echo $CUSTOMER_RESPONSE | grep -o '"id":[0-9]*' | grep -o '[0-9]*' | head -1)
echo -e "\n"

# Test 11: Obtener todos los clientes
echo "11. Obteniendo todos los clientes (GET /customers)..."
curl -X GET "${BASE_URL}/customers"
echo -e "\n"

# Test 12: Obtener un cliente específico
echo "12. Obteniendo cliente con ID ${CUSTOMER_ID} (GET /customers/${CUSTOMER_ID})..."
curl -X GET "${BASE_URL}/customers/${CUSTOMER_ID}"
echo -e "\n"

# Test 13: Actualizar cliente
echo "13. Actualizando cliente con ID ${CUSTOMER_ID} (PUT /customers/${CUSTOMER_ID})..."
curl -X PUT "${BASE_URL}/customers/${CUSTOMER_ID}" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Farmacia Central Premium",
    "address": "Calle Principal 123, Local A",
    "contact": "+34 900 123 999",
    "type_custom": "premium"
  }'
echo -e "\n"

# ==================== PROVIDERS ====================
echo "=========================================="
echo "PROBANDO ENDPOINTS DE PROVIDERS"
echo "=========================================="
echo ""

# Test 14: Crear proveedor
echo "14. Creando un nuevo proveedor (POST /providers)..."
PROVIDER_RESPONSE=$(curl -s -X POST "${BASE_URL}/providers" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Laboratorios ABC",
    "prov_license": "LIC-12345-2024",
    "address": "Polígono Industrial, Nave 5"
  }')
echo "$PROVIDER_RESPONSE"
PROVIDER_ID=$(echo $PROVIDER_RESPONSE | grep -o '"id":[0-9]*' | grep -o '[0-9]*' | head -1)
echo -e "\n"

# Test 15: Obtener todos los proveedores
echo "15. Obteniendo todos los proveedores (GET /providers)..."
curl -X GET "${BASE_URL}/providers"
echo -e "\n"

# Test 16: Obtener un proveedor específico
echo "16. Obteniendo proveedor con ID ${PROVIDER_ID} (GET /providers/${PROVIDER_ID})..."
curl -X GET "${BASE_URL}/providers/${PROVIDER_ID}"
echo -e "\n"

# ==================== PRODUCTS ====================
echo "=========================================="
echo "PROBANDO ENDPOINTS DE PRODUCTS"
echo "=========================================="
echo ""

# Test 17: Crear producto
echo "17. Creando un nuevo producto (POST /products)..."
PRODUCT_RESPONSE=$(curl -s -X POST "${BASE_URL}/products" \
  -H "Content-Type: application/json" \
  -d "{
    \"name\": \"Paracetamol 500mg\",
    \"unit\": 100,
    \"description\": \"Analgésico y antipirético\",
    \"provider_id\": ${PROVIDER_ID}
  }")
echo "$PRODUCT_RESPONSE"
PRODUCT_ID=$(echo $PRODUCT_RESPONSE | grep -o '"id":[0-9]*' | grep -o '[0-9]*' | head -1)
echo -e "\n"

# Test 18: Obtener todos los productos
echo "18. Obteniendo todos los productos (GET /products)..."
curl -X GET "${BASE_URL}/products"
echo -e "\n"

# Test 19: Obtener un producto específico
echo "19. Obteniendo producto con ID ${PRODUCT_ID} (GET /products/${PRODUCT_ID})..."
curl -X GET "${BASE_URL}/products/${PRODUCT_ID}"
echo -e "\n"

# Test 20: Actualizar producto
echo "20. Actualizando producto con ID ${PRODUCT_ID} (PUT /products/${PRODUCT_ID})..."
curl -X PUT "${BASE_URL}/products/${PRODUCT_ID}" \
  -H "Content-Type: application/json" \
  -d "{
    \"name\": \"Paracetamol 500mg (Genérico)\",
    \"unit\": 150,
    \"description\": \"Analgésico y antipirético - versión genérica\",
    \"provider_id\": ${PROVIDER_ID}
  }"
echo -e "\n"

# ==================== PAYMENTS ====================
echo "=========================================="
echo "PROBANDO ENDPOINTS DE PAYMENTS"
echo "=========================================="
echo ""

# Test 21: Crear método de pago
echo "21. Creando un nuevo método de pago (POST /payments)..."
PAYMENT_RESPONSE=$(curl -s -X POST "${BASE_URL}/payments" \
  -H "Content-Type: application/json" \
  -d '{
    "pay_mode": "Tarjeta de crédito"
  }')
echo "$PAYMENT_RESPONSE"
PAYMENT_ID=$(echo $PAYMENT_RESPONSE | grep -o '"id":[0-9]*' | grep -o '[0-9]*' | head -1)
echo -e "\n"

# Test 22: Obtener todos los métodos de pago
echo "22. Obteniendo todos los métodos de pago (GET /payments)..."
curl -X GET "${BASE_URL}/payments"
echo -e "\n"

# Test 23: Obtener un método de pago específico
echo "23. Obteniendo método de pago con ID ${PAYMENT_ID} (GET /payments/${PAYMENT_ID})..."
curl -X GET "${BASE_URL}/payments/${PAYMENT_ID}"
echo -e "\n"

# Test 24: Actualizar método de pago
echo "24. Actualizando método de pago con ID ${PAYMENT_ID} (PUT /payments/${PAYMENT_ID})..."
curl -X PUT "${BASE_URL}/payments/${PAYMENT_ID}" \
  -H "Content-Type: application/json" \
  -d '{
    "pay_mode": "Transferencia bancaria"
  }'
echo -e "\n"

# ==================== INVENTORY ====================
echo "=========================================="
echo "PROBANDO ENDPOINTS DE INVENTORY"
echo "=========================================="
echo ""

# Test 25: Crear inventario
echo "25. Creando un nuevo inventario (POST /inventory)..."
INVENTORY_RESPONSE=$(curl -s -X POST "${BASE_URL}/inventory" \
  -H "Content-Type: application/json" \
  -d "{
    \"cost\": 5.50,
    \"price\": 8.99,
    \"unit\": 100,
    \"product_id\": ${PRODUCT_ID}
  }")
echo "$INVENTORY_RESPONSE"
INVENTORY_ID=$(echo $INVENTORY_RESPONSE | grep -o '"id":[0-9]*' | grep -o '[0-9]*' | head -1)
echo -e "\n"

# Test 26: Obtener todo el inventario
echo "26. Obteniendo todo el inventario (GET /inventory)..."
curl -X GET "${BASE_URL}/inventory"
echo -e "\n"

# Test 27: Obtener un inventario específico
echo "27. Obteniendo inventario con ID ${INVENTORY_ID} (GET /inventory/${INVENTORY_ID})..."
curl -X GET "${BASE_URL}/inventory/${INVENTORY_ID}"
echo -e "\n"

# Test 28: Actualizar inventario
echo "28. Actualizando inventario con ID ${INVENTORY_ID} (PUT /inventory/${INVENTORY_ID})..."
curl -X PUT "${BASE_URL}/inventory/${INVENTORY_ID}" \
  -H "Content-Type: application/json" \
  -d "{
    \"cost\": 5.00,
    \"price\": 7.99,
    \"unit\": 150,
    \"product_id\": ${PRODUCT_ID}
  }"
echo -e "\n"

# ==================== ORDERS ====================
echo "=========================================="
echo "PROBANDO ENDPOINTS DE ORDERS"
echo "=========================================="
echo ""

# Test 29: Crear orden
echo "29. Creando una nueva orden (POST /orders)..."
ORDER_RESPONSE=$(curl -s -X POST "${BASE_URL}/orders" \
  -H "Content-Type: application/json" \
  -d "{
    \"paymentMode\": \"Tarjeta de crédito\",
    \"comment\": \"Pedido urgente\",
    \"customer_id\": ${CUSTOMER_ID},
    \"user_id\": ${USER_ID}
  }")
echo "$ORDER_RESPONSE"
ORDER_ID=$(echo $ORDER_RESPONSE | grep -o '"id":[0-9]*' | grep -o '[0-9]*' | head -1)
echo -e "\n"

# Test 30: Obtener todas las órdenes
echo "30. Obteniendo todas las órdenes (GET /orders)..."
curl -X GET "${BASE_URL}/orders"
echo -e "\n"

# Test 31: Obtener una orden específica
echo "31. Obteniendo orden con ID ${ORDER_ID} (GET /orders/${ORDER_ID})..."
curl -X GET "${BASE_URL}/orders/${ORDER_ID}"
echo -e "\n"

# Test 32: Actualizar orden
echo "32. Actualizando orden con ID ${ORDER_ID} (PUT /orders/${ORDER_ID})..."
curl -X PUT "${BASE_URL}/orders/${ORDER_ID}" \
  -H "Content-Type: application/json" \
  -d "{
    \"paymentMode\": \"Efectivo\",
    \"comment\": \"Pedido procesado\",
    \"customer_id\": ${CUSTOMER_ID},
    \"user_id\": ${USER_ID}
  }"
echo -e "\n"

# ==================== PAYMENT DETAILS ====================
echo "=========================================="
echo "PROBANDO ENDPOINTS DE PAYMENT DETAILS"
echo "=========================================="
echo ""

# Test 33: Crear detalle de pago
echo "33. Creando un nuevo detalle de pago (POST /payDetails)..."
PAYDETAIL_RESPONSE=$(curl -s -X POST "${BASE_URL}/payDetails" \
  -H "Content-Type: application/json" \
  -d "{
    \"quantity_ordered\": 10,
    \"price\": 8.99,
    \"order_id\": ${ORDER_ID},
    \"product_id\": ${PRODUCT_ID}
  }")
echo "$PAYDETAIL_RESPONSE"
PAYDETAIL_ID=$(echo $PAYDETAIL_RESPONSE | grep -o '"id":[0-9]*' | grep -o '[0-9]*' | head -1)
echo -e "\n"

# Test 34: Obtener todos los detalles de pago
echo "34. Obteniendo todos los detalles de pago (GET /payDetails)..."
curl -X GET "${BASE_URL}/payDetails"
echo -e "\n"

# Test 35: Obtener un detalle de pago específico
echo "35. Obteniendo detalle de pago con ID ${PAYDETAIL_ID} (GET /payDetails/${PAYDETAIL_ID})..."
curl -X GET "${BASE_URL}/payDetails/${PAYDETAIL_ID}"
echo -e "\n"

# Test 36: Actualizar detalle de pago
echo "36. Actualizando detalle de pago con ID ${PAYDETAIL_ID} (PUT /payDetails/${PAYDETAIL_ID})..."
curl -X PUT "${BASE_URL}/payDetails/${PAYDETAIL_ID}" \
  -H "Content-Type: application/json" \
  -d "{
    \"quantity_ordered\": 15,
    \"price\": 7.99,
    \"order_id\": ${ORDER_ID},
    \"product_id\": ${PRODUCT_ID}
  }"
echo -e "\n"

# ==================== DELETE TESTS ====================
echo "=========================================="
echo "PROBANDO ENDPOINTS DELETE"
echo "=========================================="
echo ""

# Test 37: Eliminar detalle de pago
echo "37. Eliminando detalle de pago con ID ${PAYDETAIL_ID} (DELETE /payDetails/${PAYDETAIL_ID})..."
curl -X DELETE "${BASE_URL}/payDetails/${PAYDETAIL_ID}"
echo -e "\n"

# Test 38: Eliminar orden
echo "38. Eliminando orden con ID ${ORDER_ID} (DELETE /orders/${ORDER_ID})..."
curl -X DELETE "${BASE_URL}/orders/${ORDER_ID}"
echo -e "\n"

# Test 39: Eliminar inventario
echo "39. Eliminando inventario con ID ${INVENTORY_ID} (DELETE /inventory/${INVENTORY_ID})..."
curl -X DELETE "${BASE_URL}/inventory/${INVENTORY_ID}"
echo -e "\n"

# Test 40: Eliminar método de pago
echo "40. Eliminando método de pago con ID ${PAYMENT_ID} (DELETE /payments/${PAYMENT_ID})..."
curl -X DELETE "${BASE_URL}/payments/${PAYMENT_ID}"
echo -e "\n"

# Test 41: Eliminar producto
echo "41. Eliminando producto con ID ${PRODUCT_ID} (DELETE /products/${PRODUCT_ID})..."
curl -X DELETE "${BASE_URL}/products/${PRODUCT_ID}"
echo -e "\n"

# Test 42: Eliminar cliente
echo "42. Eliminando cliente con ID ${CUSTOMER_ID} (DELETE /customers/${CUSTOMER_ID})..."
curl -X DELETE "${BASE_URL}/customers/${CUSTOMER_ID}"
echo -e "\n"

# Test 43: Eliminar actividad
echo "43. Eliminando actividad con ID ${ACTIVITY_ID} (DELETE /activities/${ACTIVITY_ID})..."
curl -X DELETE "${BASE_URL}/activities/${ACTIVITY_ID}"
echo -e "\n"

# Test 44: Eliminar usuario
echo "44. Eliminando usuario con ID ${USER_ID} (DELETE /users/${USER_ID})..."
curl -X DELETE "${BASE_URL}/users/${USER_ID}"
echo -e "\n"

echo "=========================================="
echo "PRUEBAS COMPLETADAS"
echo "=========================================="
