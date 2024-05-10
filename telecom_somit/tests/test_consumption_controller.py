from odoo.tests.common import HttpCase, tagged
import json
from datetime import datetime

@tagged('-standard', 'controller')
class TestConsumptionController(HttpCase):

    def setUp(self):
        super(TestConsumptionController, self).setUp()
        # Prepare environment and variables
        Product = self.env['product.product']
        TelecomConsumption = self.env['telecom.consumption']

        # Create a product for use in consumption records
        self.product = Product.create({
            'name': 'Test Product',
            'type': 'product'
        })

        # Create a consumption record
        self.consumption = TelecomConsumption.create({
            'timestamp': datetime.now(),
            'quantity': 10,
            'product_id': self.product.id,
        })

    def test_01_consumption_creation(self):
        """Test creation of a new consumption record via the controller."""
        data = {
            'timestamp': '2023-05-01',
            'quantity': 20,
            'product_id': self.product.id
        }
        response = self.url_open(
            '/telecom_consumptions/consumptions',
            data=json.dumps(data),
            method='POST',
            content_type='application/json'
        )
        result = json.loads(response.text)
        self.assertIn('consumption', result)
        self.assertEqual(result['consumption'][0]['quantity'], 20)
        self.assertEqual(response.status_code, 200)

    def test_02_consumption_reading(self):
        """Test reading consumption records via the controller."""
        response = self.url_open('/telecom_consumptions/consumptions')
        result = json.loads(response.text)
        self.assertIn('consumptions', result)
        self.assertIsInstance(result['consumptions'], list)
        self.assertGreater(len(result['consumptions']), 0)

    def test_03_consumption_updating(self):
        """Test updating an existing consumptionrecord."""
        new_data = {
            'timestamp': '2023-05-02',
            'quantity': 15
        }
        response = self.url_open(
            f'/telecom_consumptions/consumptions/{self.consumption.id}',
            data=json.dumps(new_data),
            method='PUT',
            content_type='application/json'
        )
        result = json.loads(response.text)
        self.assertIn('consumption', result)
        self.assertEqual(result['consumption'][0]['quantity'], 15)

    def test_04_consumption_deleting(self):
        """Test deleting a consumption record."""
        response = self.url_open(
            f'/telecom_consumptions/consumptions/{self.consumption.id}',
            method='DELETE'
        )
        self.assertEqual(response.status_code, 200)
        deleted = self.env['telecom.consumption'].browse(self.consumption.id).exists()
        self.assertFalse(deleted)