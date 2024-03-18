from .services import ProductService


class ProductController:


    def __init__(self):
        self.product_service = ProductService()


    def register_product(self, data):
        """
        Register a new product with the system.
        Args:
            data (dict): Product data including name, description, manufacturer, etc.
        Returns:
            dict: Registered product data.
        """
        return self.product_service.register_product(data)


    def update_product(self, product_id, data):
        """
        Update an existing product.
        Args:
            product_id (int): ID of the product to be updated.
            data (dict): Updated product data.
        Returns:
            dict: Updated product data.
        """
        return self.product_service.update_product(product_id, data)


    def get_product(self, product_id):
        """
        Retrieve product information by ID.
        Args:
            product_id (int): ID of the product to retrieve.
        Returns:
            dict: Product information.
        """
        return self.product_service.get_product(product_id)


    def search_product(self, product_name):
        """
        Retrieve product information by name.
        Args:
            product_name (string): name of the product to retrieve.
        Returns:
            list of dict: Product information.
        """
        return self.product_service.search_product(product_name)


    def delete_product(self, product_id):
        """
        Delete a product from the system.
        Args:
            product_id (int): ID of the product to delete.
        Returns:
            dict: Confirmation message.
        """
        return self.product_service.delete_product(product_id)

