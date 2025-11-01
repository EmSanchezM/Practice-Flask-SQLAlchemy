from config import db, ma
import bcrypt

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    logindate = db.Column(db.DateTime)

    activities = db.relationship('Activity', backref='users', lazy='dynamic')
    orders = db.relationship('Orders', backref='users', lazy='dynamic')

    def __init__(self, name, email, password, logindate):
        self.name = name
        self.email = email
        self.set_password(password)
        self.logindate = logindate

    def set_password(self, password):
        """Hashea la contraseña antes de guardarla"""
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        """Verifica si la contraseña proporcionada coincide con el hash almacenado"""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

    def __repr__(self):
        return '<User %r>' % self.name

class UserSchema(ma.Schema):
    class Meta:
        # Removemos 'password' de los campos para no exponerlo en las respuestas
        fields = ('id', 'name', 'email', 'logindate')

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String(255))
    acDate = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, activity, acDate, user_id):
        self.activity = activity
        self.acDate = acDate
        self.user_id = user_id

    def __repr__(self):
        return '<Activity %r>' % self.activity

class ActivitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'activity', 'acDate', 'user_id')

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(255))
    contact = db.Column(db.String(100))
    type_custom = db.Column(db.String(10))

    orders = db.relationship('Orders', backref='customers', lazy='dynamic')

    def __init__(self, name, address, contact, type_custom):
        self.name = name
        self.address = address
        self.contact = contact
        self.type_custom = type_custom

    def __repr__(self):
        return '<Customer %r>' % self.name

class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'contact', 'type_custom')

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime)
    pay_date = db.Column(db.DateTime)
    paymentMode = db.Column(db.Integer, db.ForeignKey('payments.id'))
    comment = db.Column(db.String(255))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, order_date, pay_date, paymentMode, comment, customer_id, user_id):
        self.order_date = order_date
        self.pay_date = pay_date
        self.paymentMode = paymentMode
        self.comment = comment
        self.customer_id = customer_id
        self.user_id = user_id

class OrderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'order_date', 'pay_date', 'paymentMode', 'comment', 'customer_id','user_id')

class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pay_mode = db.Column(db.String(25))
    orders = db.relationship('Orders', backref='payments', lazy='dynamic')

    def __init__(self, pay_mode):
        self.pay_mode = pay_mode
    
    def __repr__(self):
        return '<Payments %r>' % self.pay_mode

class PaymentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'pay_mode')

class PaymentDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity_ordered = db.Column(db.Integer)
    price = db.Column(db.Float())
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __init__(self, quantity_ordered, price, order_id, product_id):
        self.quantity_ordered = quantity_ordered
        self.price = price
        self.order_id = order_id
        self.product_id = product_id

class PaymentDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'quantity_ordered', 'price', 'order_id','product_id')

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    unit = db.Column(db.Integer)
    description = db.Column(db.String(255))
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'))
    paymentdetails = db.relationship('PaymentDetail', backref='products', lazy='dynamic')
    inventories = db.relationship('Inventory', backref='products', lazy='dynamic')

    def __init__(self, name, unit, description, provider_id):
        self.name = name
        self.unit = unit
        self.description = description
        self.provider_id = provider_id
    
    def __repr__(self):
        return '<Product %r>' % self.name

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'unit', 'description', 'provider_id')

class Providers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    prov_license = db.Column(db.String(100))
    address = db.Column(db.String(255))
    products = db.relationship('Products', backref='providers', lazy='dynamic')

    def __init__(self, name, prov_license, address):
        self.name = name
        self.prov_license = prov_license
        self.address = address
    
    def __repr__(self):
        return '<Provider %r>' % self.name

class ProviderSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'prov_license', 'address')

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float())
    price = db.Column(db.Float())
    unit = db.Column(db.Integer)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    def __init__(self, cost, price, unit, product_id):
        self.cost = cost
        self.price = price
        self.unit = unit
        self.product_id = product_id

class InventorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'cost', 'price', 'unit', 'product_id')

#Instancias
user_schema = UserSchema()
users_schema = UserSchema(many=True)

activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)

customer_Schema = CustomerSchema()
customers_Schema = CustomerSchema(many=True)

Order_Schema = OrderSchema()
Orders_Schema = OrderSchema(many=True)

payment_Schema = PaymentSchema()
payments_Schema = PaymentSchema(many=True)

paymentDetail_Schema = PaymentDetailSchema()
paymentDetails_Schema = PaymentDetailSchema(many=True)

product_Schema = ProductSchema()
products_Schema = ProductSchema(many=True)

provider_Schema = ProviderSchema()
providers_Schema = ProviderSchema(many=True)

inventory_Schema = InventorySchema()
inventories_Schema = InventorySchema(many=True)