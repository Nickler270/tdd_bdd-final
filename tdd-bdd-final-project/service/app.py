# service/app.py
from flask import Flask
from service.models import Product, Category  # Import models from the `service` module
from service.routes import get_products, update_products, delete_products, list_products  # Import routes

# Initialize the Flask app
app = Flask(__name__)

# Register routes
app.add_url_rule("/products/<int:product_id>", view_func=get_products, methods=["GET"])
app.add_url_rule("/products/<int:product_id>", view_func=update_products, methods=["PUT"])
app.add_url_rule("/products/<int:product_id>", view_func=delete_products, methods=["DELETE"])
app.add_url_rule("/products", view_func=list_products, methods=["GET"])

if __name__ == "__main__":
    app.run(debug=True)