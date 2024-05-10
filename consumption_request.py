import requests
import json

#script to test endpoint for CRUD consumption

# Configuration
base_url = 'http://localhost:8069'  # Change this to the URL where your Odoo server is running
login_url = f"{base_url}/web/session/authenticate"
api_url = f"{base_url}/telecom_consumptions/consumptions"
headers = {'Content-type': 'application/json'}

# Odoo credentials
payload = {
    'params': {
        'db': 'somit',  # Replace with your database name
        'login': 'admin',  # Replace with your username
        'password': 'a'  # Replace with your password
    }
}

# Start a session
session = requests.Session()

# Log in
response = session.post(login_url, data=json.dumps(payload), headers=headers)
if response.status_code == 200:
    print("Login successful!")
else:
    print("Failed to log in")

# Test POST - Create a new consumption record
new_consumption = {
    "timestamp": "1605892270",  # Example UNIX timestamp
    "quantity": 13,
    "product_id": 2
}

response = session.post(api_url, data=json.dumps(new_consumption), headers=headers)
if response.status_code == 200:
    print("Creation successful:", response.text)
else:
    print("Failed to create record")

# Test GET - Retrieve consumption records
response = session.get(api_url)
if response.status_code == 200:
    print("Retrieval successful:", response.text)
else:
    print("Failed to retrieve records")

# Assuming we know the ID of the consumption to update or delete
consumption_id = 8  # This should be replaced with an actual ID from your database

# Test PUT - Update a consumption record
updated_consumption = {
    "quantity": 10
}

response = session.put(f"{api_url}/{consumption_id}", data=json.dumps(updated_consumption), headers=headers)
if response.status_code == 200:
    print("Update successful:", response.text)
else:
    print("Failed to update record")

# Test DELETE - Delete a consumption record
response = session.delete(f"{api_url}/{consumption_id}")
if response.status_code == 200:
    print("Deletion successful:", response.text)
else:
    print("Failed to delete record")

# Closing the session
session.close()
