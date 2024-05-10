# SomIT

#Documentation for Telecom Consumption Module

## Overview
The Telecom Consumption module provides a RESTful API for managing telecom consumption records within Odoo. This includes operations to create, retrieve, update, and delete consumption records.

## Endpoints

### ____GET /telecom_consumptions/consumptions____

Retrieve a list of all consumption records. 

**Permissions**: Requires user authentication.

#### **Response**:
•	200 OK - Successfully retrieved list of consumptions.

•	Content-type: application/json

•	**Response Body**:

{
  ``"consumptions": [
    {
      "id": 1,`
      "timestamp": "2023-05-01",
      "quantity": 10,
      "product_id": 2
    }``
}

### **POST /telecom_consumptions/consumptions**
Create a new consumption record.

**Permissions**: Requires user authentication.

**Request Body:**

•	Content-type: application/json

•	**Body**:

{
`  "timestamp": "2023-05-01",
  "quantity": 20,
  "product_id": 2`
}

#### **Response:**

•	200 OK - Successfully created a new consumption record.

•	Content-type: application/json

•	**Response Body:**

{
 ` "consumption": [
    {
      "id": 3,
      "timestamp": "2023-05-01",
      "quantity": 20,
      "product_id": 2
    }
  ]`
}

### PUT /telecom_consumptions/consumptions/<id>

Update an existing consumption record.

**Permissions**: Requires user authentication.

**URL Parameters:**

•	id (int) - The ID of the consumption record to update.

**Request Body:**

•	Content-type: application/json

•	**Body**:

{
`
  "timestamp": "2023-05-02",
  "quantity": 15`
}

**Response:**

•	200 OK - Successfully updated the consumption record.

•	Content-type: application/json

**•	Response Body:**

{
  `"consumption": [
    {
      "id": 1,
      "timestamp": "2023-05-02",
      "quantity": 15,
      "product_id": 2
    }`
}

### DELETE /telecom_consumptions/consumptions/<id>

Delete a consumption record.

**Permissions**: Requires user authentication.

**URL Parameters:**

•	id (int) - The ID of the consumption record to delete.

**Response**:

•	200 OK - Successfully deleted the consumption record.

## Manual Testing

Create python script `consumption_request.py` to test Odoo controller Endpoint.
 

The script uses the requests library to perform an HTTP GET request to a predefined Odoo controller endpoint.

It captures and prints the HTTP status code and response body to allow for easy debugging and verification of the endpoint's output.

The script is useful for automated testing during development or deployment phases to ensure continuous integration and delivery processes.

## Unit Tests

### **Test Cases**

The unit tests cover the following functionalities:

1.	Test Creation of Consumption Record (test_01_consumption_creation):

      •	Validates the successful creation of a consumption record via the POST method.
2.	Test Retrieval of Consumption Records (test_02_consumption_reading):

      •	Checks the successful retrieval of all consumption records using the GET method.
      
3.	Test Updating a Consumption Record (test_03_consumption_updating):
  
      •	Ensures that an existing consumption record can be updated using the PUT method.
4.	Test Deletion of a Consumption Record (test_04_consumption_deleting):

      •	Confirms that a consumption record can be deleted using the DELETE method.

Running the Tests
To run these tests, execute the following command in your Odoo instance:

odoo-bin --addons-path=<path_to_addons> --db-filter=mydb -i telecom_somit --test-enable --log-level=test





