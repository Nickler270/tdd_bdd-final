#features/tests/test_models.py
import unittest
from service.models import Product, db
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):
    """Test Cases for Product Model"""

    @classmethod
    def setUpClass(cls):
        """Set up the test database"""
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test database"""
        db.drop_all()

    def setUp(self):
        """Start each test with a clean database"""
        db.session.query(Product).delete()
        db.session.commit()

    def tearDown(self):
        """Clean up after each test"""
        db.session.remove()

    def test_read_a_product(self):
        """It should Read a Product"""
        product = ProductFactory()
        product.id = None
        product.create()
        self.assertIsNotNone(product.id)

        # Fetch it back
        found_product = Product.find(product.id)
        self.assertEqual(found_product.id, product.id)
        self.assertEqual(found_product.name, product.name)
        self.assertEqual(found_product.description, product.description)
        self.assertEqual(found_product.price, product.price)

    def test_update_a_product(self):
        """It should Update a Product"""
        product = ProductFactory()
        product.id = None
        product.create()
        self.assertIsNotNone(product.id)

        # Change it and save it
        product.description = "New Description"
        original_id = product.id
        product.update()

        self.assertEqual(product.id, original_id)
        self.assertEqual(product.description, "New Description")

        # Fetch it back and make sure the id hasn't changed
        products = Product.all()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].id, original_id)
        self.assertEqual(products[0].description, "New Description")

    def test_delete_a_product(self):
        """It should Delete a Product"""
        product = ProductFactory()
        product.create()
        self.assertEqual(len(Product.all()), 1)

        # Delete the product
        product.delete()
        self.assertEqual(len(Product.all()), 0)

    def test_list_all_products(self):
        """It should List all Products in the database"""
        products = Product.all()
        self.assertEqual(products, [])

        # Create 5 products
        for _ in range(5):
            product = ProductFactory()
            product.create()

        # Fetch all products
        products = Product.all()
        self.assertEqual(len(products), 5)

    def test_find_by_name(self):
        """It should Find a Product by Name"""
        products = ProductFactory.create_batch(5)
        for product in products:
            product.create()

        name = products[0].name
        count = len([product for product in products if product.name == name])
        found = Product.find_by_name(name)

        self.assertEqual(found.count(), count)
        for product in found:
            self.assertEqual(product.name, name)

    def test_find_by_availability(self):
        """It should Find Products by Availability"""
        products = ProductFactory.create_batch(10)
        for product in products:
            product.create()

        available = products[0].available
        count = len([product for product in products if product.available == available])
        found = Product.find_by_availability(available)

        self.assertEqual(found.count(), count)
        for product in found:
            self.assertEqual(product.available, available)

    def test_find_by_category(self):
        """It should Find Products by Category"""
        products = ProductFactory.create_batch(10)
        for product in products:
            product.create()

        category = products[0].category
        count = len([product for product in products if product.category == category])
        found = Product.find_by_category(category)

        self.assertEqual(found.count(), count)
        for product in found:
            self.assertEqual(product.category, category)
