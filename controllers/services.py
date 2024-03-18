from .repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repo = ProductRepository()

    def register_product(self, data):
        """
        Register a new product with the system.
        Args:
            data (dict): Product data including name, description, manufacturer, etc.
        Returns:
            dict: Registered product data.
        """
        # Implement validation logic here if needed
        return self.product_repo.create_product(data)

    def update_product(self, product_id, data):
        """
        Update an existing product.
        Args:
            product_id (int): ID of the product to be updated.
            data (dict): Updated product data.
        Returns:
            dict: Updated product data.
        """
        # Implement validation logic here if needed
        return self.product_repo.update_product(product_id, data)

    def search_product(self, product_name):
        """
        Retrieve product information by name or other details.
        Args:
            product_name (string): name of the product to retrieve.
        Returns:
            dict: Product information.
            {"product_list":[]}
        """
        return self.product_repo.search_product_by_name(product_name)

    def get_product(self, product_id):
        """
        Retrieve product information by ID.
        Args:
            product_id (int): ID of the product to retrieve.
        Returns:
            dict: Product information.
        """
        return self.product_repo.get_product(product_id)

    def delete_product(self, product_id):
        """
        Delete a product from the system.
        Args:
            product_id (int): ID of the product to delete.
        Returns:
            dict: Confirmation message.
        """
        return self.product_repo.delete_product(product_id)

