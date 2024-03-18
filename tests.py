import requests

BASE_URL = 'http://10.0.2.17:5000'  # Update with your actual base URL

def get_access_token():
    """
    Retrieves an access token by sending a POST request to the login endpoint.
    
    Returns:
        str: Access token for authentication.
    
    Raises:
        ValueError: If the request fails or the access token cannot be retrieved.
    """
    url = f'{BASE_URL}/login'
    data = {'username': 'admin', 'password': 'admin123'}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise ValueError("Failed to retrieve access token")

def test_register_product(access_token):
    """
    Tests the registration of a new product.
    
    Args:
        access_token (str): Access token for authentication.
    """
    url = f'{BASE_URL}/products'
    data = {
        'name': 'Test Product',
        'description': 'Test Description',
        'manufacturer': 'Test Manufacturer',
        'serial_number': '12345',
        'date_manufacture': '2024-03-15',
        'warranty_information': 'Test Warranty',
        'category': 'Test Category'
    }
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.post(url, json=data, headers=headers)
    print("register")
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == 'Test Product'

def test_update_product(access_token):
    """
    Tests the update of an existing product.
    
    Args:
        access_token (str): Access token for authentication.
    """
    product_id = 1  # Assuming product with ID 1 exists
    url = f'{BASE_URL}/products/{product_id}'
    data = {
        'name': 'Updated Product',
        'description': 'Updated Description',
        'manufacturer': 'Updated Manufacturer',
        'serial_number': '54321',
        'date_manufacture': '2024-03-20',
        'warranty_information': 'Updated Warranty',
        'category': 'Updated Category'
    }
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.put(url, json=data, headers=headers)
    print("put")
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'Updated Product'

def test_get_product(access_token):
    """
    Tests the retrieval of a product.
    
    Args:
        access_token (str): Access token for authentication.
    """
    product_id = 1  # Assuming product with ID 1 exists
    url = f'{BASE_URL}/products/{product_id}'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    print("get")
    print(response.json())
    assert response.status_code == 200
    assert response.json()['id'] == 1

def test_delete_product(access_token, product_id):
    """
    Tests the deletion of a product.
    
    Args:
        access_token (str): Access token for authentication.
        product_id (int): ID of the product to delete.
    """
    url = f'{BASE_URL}/products/{product_id}'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.delete(url, headers=headers)
    print("delete")
    print(response.json())
    assert response.status_code == 200
    assert response.json()['message'] == 'Product deleted successfully'

def test_search_product(access_token, name):
    """
    Tests the search for a product by name.
    
    Args:
        access_token (str): Access token for authentication.
        name (str): Name of the product to search for.
    """
    url = f'{BASE_URL}/products?name={name}' # Assuming 'test' is a search query
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    print("search")
    print(response.json())
    if name == 'flag_false':
        assert response.status_code == 400
        assert response.json()['error'] == "Product not found"  # Assuming it returns at least one result
    else:
        assert response.status_code == 200
        assert len(response.json()) > 0

if __name__ == '__main__':
    access_token = get_access_token()
    test_register_product(access_token)
    test_get_product(access_token)
    test_update_product(access_token)
    test_search_product(access_token, 'test')
    test_delete_product(access_token, 1)
    print("All tests passed!")
