from odoo import http, _
from odoo.http import request
import json
from datetime import datetime

class ConsumptionController(http.Controller):

    @http.route('/telecom_consumptions/consumptions', auth='user', methods=['GET'], csrf=False)
    def get_consumption_data(self, **kw):
        consumptions = request.env['telecom.consumption'].sudo().search([])
        # Convert dates to strings for serialization
        consumptions_data = [{
            'id': c.id,
            'timestamp': c.timestamp.strftime('%Y-%m-%d %H:%M:%S'),  # Convert date to string
            'quantity': c.quantity,
            'product_id': c.product_id.id,
        } for c in consumptions]
        return json.dumps({'consumptions': consumptions_data})

    @http.route('/telecom_consumptions/consumptions', auth='user', methods=['POST'], csrf=False)
    def create_consumption(self, **kw):
        try:
            data = json.loads(request.httprequest.data)
            # Convert date string to datetime object
            data['timestamp'] = datetime.utcfromtimestamp(int(data['timestamp']))
            data['timestamp'] = data['timestamp'].strftime('%Y-%m-%d')
            consumption = request.env['telecom.consumption'].sudo().create(data)
            return json.dumps({'consumption': consumption.read()})
        except Exception as e:
            return json.dumps({'error': str(e)})

    @http.route('/telecom_consumptions/consumptions/<int:id>', auth='user', methods=['GET'], csrf=False)
    def get_consumption(self, id, **kw):
        consumption = request.env['telecom.consumption'].sudo().browse(id)
        if not consumption.exists():
            return json.dumps({'error': 'Consumption not found'})
        consumption_data = {
            'id': consumption.id,
            'timestamp': consumption.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'quantity': consumption.quantity,
            'product_id': consumption.product_id.id,
        }
        return json.dumps({'consumption': consumption_data})

    @http.route('/telecom_consumptions/consumptions/<int:id>', auth='user', methods=['PUT'], csrf=False)
    def update_consumption(self, id, **kw):
        consumption = request.env['telecom.consumption'].sudo().browse(id)
        if not consumption.exists():
            return json.dumps({'error': 'Consumption not found'})
        try:
            data = json.loads(request.httprequest.data)
            if 'timestamp' in data:
                data['timestamp'] = datetime.utcfromtimestamp(int(data['timestamp']))
            consumption.write(data)
            return json.dumps({'consumption': consumption.read(['id', 'timestamp', 'quantity', 'product_id'])})
        except Exception as e:
            return json.dumps({'error': str(e)})

    @http.route('/telecom_consumptions/consumptions/<int:id>', auth='user', methods=['DELETE'], csrf=False)
    def delete_consumption(self, id, **kw):
        # Delete a specific consumption record by its ID
        consumption = request.env['telecom.consumption'].sudo().browse(id)
        consumption.unlink()
        # Return success message
        return json.dumps({'message': 'Consumption deleted successfully.'})