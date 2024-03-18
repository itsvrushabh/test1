class ProductRepository:
    """Repository for managing Product objects in the database."""

    def create_product(self, data):
        """
        Creates a new product and saves it to the database.

        Args:
            data (dict): A dictionary containing product data.

        Returns:
            dict: Serialized representation of the created product.

        Example:
            product_data = {
                'name': 'Product 1',
                'description': 'Description of Product 1',
                'manufacturer': 'Manufacturer 1',
                'serial_number': '123456',
                'date_manufacture': '2023-01-01',
                'warranty_information': '1 year warranty',
                'category': 'Electronics'
            }
            product_repository.create_product(product_data)
        """
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return product.serialize()

    def update_product(self, product_id, data):
        """
        Updates an existing product in the database.

        Args:
            product_id (int): The ID of the product to be updated.
            data (dict): A dictionary containing updated product data.

        Returns:
            dict: Serialized representation of the updated product.

        Raises:
            ValueError: If the product with the specified ID is not found.

        Example:
            updated_data = {
                'name': 'Updated Product',
                'description': 'Updated description',
                'manufacturer': 'Updated Manufacturer',
                'category': 'Updated Category'
            }
            product_repository.update_product(1, updated_data)
        """
        product = Product.query.get(product_id)
        if product:
            for key, value in data.items():
                setattr(product, key, value)
            db.session.commit()
            return product.serialize()
        else:
            raise ValueError("Product not found")

    def get_product(self, product_id):
        """
        Retrieves a product by ID from the database.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            dict: Serialized representation of the retrieved product, or None if not found.

        Example:
            product_repository.get_product(1)
        """
        product = Product.query.get(product_id)
        if product:
            return product.serialize()
        else:
            return None

    def search_product_by_name(self, product_name):
        """
        Searches products by name in the database.

        Args:
            product_name (str): The name or part of the name to search for.

        Returns:
            dict: A dictionary containing a list of serialized products matching the search query.

        Raises:
            ValueError: If no products are found matching the search query.

        Example:
            product_repository.search_product_by_name('Product')
        """
        products = Product.query.filter(Product.name.ilike(f'%{product_name}%')).all()
        if products:
            return {'product_list': [product.serialize() for product in products]}
        else:
            raise ValueError("Product not found")

    def delete_product(self, product_id):
        """
        Deletes a product by ID from the database.

        Args:
            product_id (int): The ID of the product to delete.

        Returns:
            dict: A dictionary containing a message indicating the success of the deletion.

        Raises:
            ValueError: If the product with the specified ID is not found.

        Example:
            product_repository.delete_product(1)
        """
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return {"message": "Product deleted successfully"}
        else:
            raise ValueError("Product not found")