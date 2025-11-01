from flask import request, jsonify
from datetime import datetime
from models import *
from config import app 

@app.route('/users', methods=['POST'])
def addUser():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    logindate = datetime.today()

    new_user = Users(name, email, password, logindate)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@app.route('/users', methods=['GET'])
def getUsers():
    all_users = Users.query.all()
    result = users_schema.dump(all_users)

    return jsonify(result)

@app.route('/users/<id>', methods=['GET'])
def getUser(id):
    user = Users.query.get(id)
    return user_schema.jsonify(user)

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = Users.query.get(id)

    name = request.json['name']
    email = request.json['email']
    logindate = datetime.today()

    user.name = name
    user.email = email 
    
    # Solo actualizar la contraseña si se proporciona
    if 'password' in request.json and request.json['password']:
        user.set_password(request.json['password'])
    
    user.logindate = logindate

    db.session.commit()

    return user_schema.jsonify(user)

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = Users.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)

@app.route('/users/login', methods=['POST'])
def login_user():
    """Endpoint para autenticar usuarios"""
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return jsonify({'error': 'Email y contraseña son requeridos'}), 400

        user = Users.query.filter_by(email=email).first()

        if user and user.check_password(password):
            # Actualizar fecha de login
            user.logindate = datetime.today()
            db.session.commit()
            return jsonify({
                'message': 'Login exitoso',
                'user': user_schema.dump(user)
            }), 200
        else:
            return jsonify({'error': 'Email o contraseña incorrectos'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/activities', methods=['POST'])
def addActivity():
    activity = request.json['activity']
    acDate = datetime.today()
    user_id = request.json['user_id']

    new_activity = Activity(activity, acDate, user_id)
    db.session.add(new_activity)
    db.session.commit()

    return activity_schema.jsonify(new_activity)

@app.route('/activities', methods=['GET'])
def getActivities():
    all_activities = Activity.query.all()
    result = activities_schema.dump(all_activities)
    return jsonify(result)

@app.route('/activities/<id>', methods=['GET'])
def getActivity(id):
    activity = Activity.query.get(id)
    return activity_schema.jsonify(activity)

@app.route('/activities/<id>', methods=['PUT'])
def update_activity(id):
    activity = Activity.query.get(id)

    activity_text = request.json['activity']
    acDate = datetime.today()
    user_id = request.json['user_id']

    activity.activity = activity_text
    activity.acDate = acDate
    activity.user_id = user_id

    db.session.commit()

    return activity_schema.jsonify(activity)

@app.route('/activities/<id>', methods=['DELETE'])
def delete_activity(id):
    activity = Activity.query.get(id)
    db.session.delete(activity)
    db.session.commit()

    return activity_schema.jsonify(activity)

@app.route('/customers', methods=['POST'])
def addCustomer():
    name = request.json['name']
    address = request.json['address']
    contact = request.json['contact']
    type_custom = request.json['type_custom']

    new_customer = Customers(name, address, contact, type_custom)

    db.session.add(new_customer)
    db.session.commit()

    return customer_Schema.jsonify(new_customer)

@app.route('/customers', methods=['GET'])
def getCustomers():
    all_customers = Customers.query.all()
    result = customers_Schema.dump(all_customers)
    return jsonify(result)

@app.route('/customers/<id>', methods=['GET'])
def getCustomer(id):
    customer = Customers.query.get(id)
    return customer_Schema.jsonify(customer)

@app.route('/customers/<id>', methods=['PUT'])
def update_customer(id):
    customer = Customers.query.get(id)

    name = request.json['name']
    address = request.json['address']
    contact = request.json['contact']
    type_custom = request.json['type_custom']

    customer.name = name
    customer.address = address
    customer.contact = contact
    customer.type_custom = type_custom

    db.session.commit()

    return customer_Schema.jsonify(customer)

@app.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customers.query.get(id)
    db.session.delete(customer)
    db.session.commit()

    return customer_Schema.jsonify(customer)

@app.route('/providers', methods=['POST'])
def addProvider():
    name = request.json['name']
    prov_license = request.json['prov_license']
    address = request.json['address']

    new_provider = Providers(name, prov_license, address)
    db.session.add(new_provider)
    db.session.commit()

    return provider_Schema.jsonify(new_provider)
    
@app.route('/providers', methods=['GET'])
def getProviders():
    all_providers = Providers.query.all()
    result = providers_Schema.dump(all_providers)
    return jsonify(result)

@app.route('/providers/<id>', methods=['GET'])
def getProvider(id):
    provider = Providers.query.get(id)
    return provider_Schema.jsonify(provider)

@app.route('/providers/<id>', methods=['PUT'])
def update_provider(id):
    provider = Providers.query.get(id)

    name = request.json['name']
    prov_license = request.json['prov_license']
    address = request.json['address']

    provider.name = name
    provider.prov_license = prov_license
    provider.address = address

    db.session.commit()

    return provider_Schema.jsonify(provider)

@app.route('/providers/<id>', methods=['DELETE'])
def delete_provider(id):
    provider = Providers.query.get(id)
    db.session.delete(provider)
    db.session.commit()

    return provider_Schema.jsonify(provider)

@app.route('/products', methods=['POST'])
def addProducts():
    name = request.json['name']
    unit = request.json['unit']
    description = request.json['description']
    provider_id = request.json['provider_id']

    new_product = Products(name, unit, description, provider_id)
    db.session.add(new_product)
    db.session.commit()

    return product_Schema.jsonify(new_product)
    
@app.route('/products', methods=['GET'])
def getProducts():
    all_products = Products.query.all()
    result = products_Schema.dump(all_products)
    return jsonify(result)

@app.route('/products/<id>', methods=['GET'])
def getProduct(id):
    product = Products.query.get(id)
    return product_Schema.jsonify(product)

@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    product = Products.query.get(id)
    
    name = request.json['name']
    unit = request.json['unit']
    description = request.json['description']
    provider_id = request.json['provider_id']

    product.name = name
    product.unit = unit
    product.description = description
    product.provider_id = provider_id

    db.session.commit()

    return product_Schema.jsonify(product)

@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Products.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_Schema.jsonify(product)

@app.route('/orders', methods=['POST'])
def addOrder():
    order_date = datetime.today()
    pay_date = datetime.today()
    paymentMode = request.json['paymentMode']
    comment = request.json['comment']
    customer_id = request.json['customer_id']
    user_id = request.json['user_id']

    new_Order = Orders(order_date, pay_date, paymentMode, comment, customer_id, user_id)
    db.session.add(new_Order)
    db.session.commit()

    return Order_Schema.jsonify(new_Order)

@app.route('/orders', methods=['GET'])
def getOrders():
    all_orders = Orders.query.all()
    result = Orders_Schema.dump(all_orders)
    return jsonify(result)

@app.route('/orders/<id>', methods=['GET'])
def getOrder(id):
    order = Orders.query.get(id)
    return Order_Schema.jsonify(order)

@app.route('/orders/<id>', methods=['PUT'])
def update_order(id):
    order = Orders.query.get(id)

    order_date = datetime.today()
    pay_date = datetime.today()
    paymentMode = request.json['paymentMode']
    comment = request.json['comment']
    customer_id = request.json['customer_id']
    user_id = request.json['user_id']

    order.order_date = order_date
    order.pay_date = pay_date
    order.paymentMode = paymentMode
    order.comment = comment
    order.customer_id = customer_id
    order.user_id = user_id

    db.session.commit()

    return Order_Schema.jsonify(order)

@app.route('/orders/<id>', methods=['DELETE'])
def delete_order(id):
    order = Orders.query.get(id)
    db.session.delete(order)
    db.session.commit()
    return Order_Schema.jsonify(order)

@app.route('/payments', methods=['POST'])
def addPayment():
    pay_mode = request.json['pay_mode']

    new_payment = Payments(pay_mode)
    db.session.add(new_payment)
    db.session.commit()

    return payment_Schema.jsonify(new_payment)

@app.route('/payments', methods=['GET'])
def getPayments():
    all_payments = Payments.query.all()
    result = payments_Schema.dump(all_payments)
    return jsonify(result)

@app.route('/payments/<id>', methods=['GET'])
def getPayment(id):
    payment = Payments.query.get(id)
    return payment_Schema.jsonify(payment)

@app.route('/payments/<id>', methods=['PUT'])
def update_payment(id):
    payment = Payments.query.get(id)

    pay_mode = request.json['pay_mode']

    payment.pay_mode = pay_mode

    db.session.commit()

    return payment_Schema.jsonify(payment)

@app.route('/payments/<id>', methods=['DELETE'])
def delete_payments(id):
    payment = Payments.query.get(id)
    db.session.delete(payment)
    db.session.commit()

    return payment_Schema.jsonify(payment)

@app.route('/payDetails', methods=['POST'])
def addPayDetails():
    quantity_ordered = request.json['quantity_ordered']
    price = request.json['price']
    order_id = request.json['order_id']
    product_id = request.json['product_id']

    new_payDetail = PaymentDetail(quantity_ordered, price, order_id, product_id)
    db.session.add(new_payDetail)
    db.session.commit()

    return paymentDetail_Schema.jsonify(new_payDetail)

@app.route('/payDetails', methods=['GET'])
def getPayDetails():
    all_payDetails = PaymentDetail.query.all()
    result = paymentDetails_Schema.dump(all_payDetails)
    return jsonify(result)

@app.route('/payDetails/<id>', methods=['GET'])
def getPayDetail(id):
    payDetail = PaymentDetail.query.get(id)
    return paymentDetail_Schema.jsonify(payDetail)

@app.route('/payDetails/<id>', methods=['PUT'])
def update_payDetails(id):
    payDetail = PaymentDetail.query.get(id)

    quantity_ordered = request.json['quantity_ordered']
    price = request.json['price']
    order_id = request.json['order_id']
    product_id = request.json['product_id']

    payDetail.quantity_ordered = quantity_ordered
    payDetail.price = price
    payDetail.order_id = order_id
    payDetail.product_id = product_id

    db.session.commit()

    return paymentDetail_Schema.jsonify(payDetail)

@app.route('/payDetails/<id>', methods=['DELETE'])
def delete_payDetails(id):
    payDetail = PaymentDetail.query.get(id)
    db.session.delete(payDetail)
    db.session.commit()

    return paymentDetail_Schema.jsonify(payDetail)

@app.route('/inventory', methods=['POST'])
def addInventory():
    cost = request.json['cost']
    price = request.json['price']
    unit = request.json['unit']
    product_id = request.json['product_id']

    new_inventory = Inventory(cost, price, unit, product_id)

    db.session.add(new_inventory)
    db.session.commit()

    return inventory_Schema.jsonify(new_inventory)

@app.route('/inventory', methods=['GET'])
def getInventories():
    all_inventories = Inventory.query.all()
    result = inventories_Schema.dump(all_inventories)
    return jsonify(result) 

@app.route('/inventory/<id>', methods=['GET'])
def getInventory(id):
    inventory = Inventory.query.get(id)
    return inventory_Schema.jsonify(inventory)

@app.route('/inventory/<id>', methods=['PUT'])
def update_inventory(id):
    inventory = Inventory.query.get(id)

    cost = request.json['cost']
    price = request.json['price']
    unit = request.json['unit']
    product_id = request.json['product_id']

    inventory.cost = cost
    inventory.price = price
    inventory.unit = unit
    inventory.product_id = product_id

    db.session.commit()

    return inventory_Schema.jsonify(inventory) 

@app.route('/inventory/<id>', methods=['DELETE'])
def delete_inventory(id):
    inventory = Inventory.query.get(id)
    db.session.delete(inventory)
    db.session.commit()

    return inventory_Schema.jsonify(inventory)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to API Pharmacy'})
