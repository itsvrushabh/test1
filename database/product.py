from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    """Product Model representing products in the database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    manufacturer = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(50), unique=True, nullable=False)
    date_manufacture = db.Column(db.Date)
    warranty_information = db.Column(db.String(200))
    category = db.Column(db.String(50))

    def serialize(self):
        """
        Serializes the Product object into a dictionary.

        Returns:
            dict: Serialized representation of the Product object.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'manufacturer': self.manufacturer,
            'serial_number': self.serial_number,
            'date_manufacture': self.date_manufacture,
            'warranty_information': self.warranty_information,
            'category': self.category
        }