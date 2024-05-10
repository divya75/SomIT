from odoo import models, fields,api


class ProductCategory(models.Model):
    _inherit = 'product.category'

    code = fields.Char(string='Code')

# Define a model for tracking telecom service consumption
class TelecomConsumption(models.Model):
    _name = 'telecom.consumption'
    _description = 'Telecom Service Consumption'

    # Overrides the name_get method to customize how records of this model are displayed.
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.timestamp} - {record.product_id.name} - {record.quantity}"
            result.append((record.id, name))
        return result

    timestamp = fields.Date(string='Timestamp')
    product_id = fields.Many2one('product.template', string='Product', required=True)
    quantity = fields.Float(string='Quantity')
    # Computed field to store the category code, which is automatically retrieved from the related product category.
    category_code = fields.Char(string='Category Code', related='product_id.categ_id.code', store=True)

    @api.depends('product_id','product_id.categ_id')
    def _compute_computed_field(self):
        for record in self:
            record.category_code = record.product_id.categ_id.code

    @api.onchange('product_id')
    def _onchange_field_one_two(self):
        for record in self:
            record.category_code = record.product_id.categ_id.code