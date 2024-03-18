from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

from database.product import db  # Importing the database instance
from controllers.product import ProductController  # Importing the ProductController

app = Flask(__name__)

# JWT configuration
app.config['JWT_SECRET_KEY'] = 'super-secret'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://myuser:mypassword@10.0.2.17:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize JWT extension
jwt = JWTManager(app)

# Initialize ProductController
product_controller = ProductController()

@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint to authenticate users and generate JWT token.

    Request Parameters:
        - username (str): The username of the user.
        - password (str): The password of the user.

    Returns:
        - JSON: JWT token if authentication is successful, else error message.
    """
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != 'admin' or password != 'admin123':
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/products', methods=['POST'])
@jwt_required()  # Requires JWT token for authentication
def register_product():
    """
    Endpoint to register a new product.

    Request Parameters:
        - JSON Data: Product details including name, price, etc.

    Returns:
        - JSON: Registered product details.
    """
    data = request.json
    try:
        product = product_controller.register_product(data)
        return jsonify(product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()  # Requires JWT token for authentication
def update_product(product_id):
    """
    Endpoint to update an existing product.

    Request Parameters:
        - product_id (int): The ID of the product to be updated.
        - JSON Data: Updated product details.

    Returns:
        - JSON: Updated product details.
    """
    data = request.json
    try:
        product = product_controller.update_product(product_id, data)
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/products/<int:product_id>', methods=['GET'])
@jwt_required()  # Requires JWT token for authentication
def get_product(product_id):
    """
    Endpoint to retrieve a specific product by ID.

    Request Parameters:
        - product_id (int): The ID of the product to retrieve.

    Returns:
        - JSON: Retrieved product details.
    """
    try:
        product = product_controller.get_product(product_id)
        if product:
            return jsonify(product), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/products', methods=['GET'])
@jwt_required()  # Requires JWT token for authentication
def search_products():
    """
    Endpoint to search for products based on name.

    Request Parameters:
        - name (str): The name of the product to search for.

    Returns:
        - JSON: List of products matching the search criteria.
    """
    try:
        name = request.args.get('name')

        if name:
            products = product_controller.search_product(name)
            return jsonify(products), 200
        else:
            return jsonify({"error": "No search criteria provided"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()  # Requires JWT token for authentication
def delete_product(product_id):
    """
    Endpoint to delete a product by ID.

    Request Parameters:
        - product_id (int): The ID of the product to delete.

    Returns:
        - JSON: Success message upon deletion.
    """
    try:
        response = product_controller.delete_product(product_id)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Database initialization
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(host='0.0.0.0', debug=True)
