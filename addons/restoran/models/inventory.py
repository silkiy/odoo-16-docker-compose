from odoo import models, fields, api

class KitchenInventory(models.Model):
    _name = 'restaurant.kitchen.inventory'
    _description = 'Kitchen Inventory'

    ingredient_name = fields.Char(string='Ingredient', required=True)
    stock_quantity = fields.Float(string='Stock Quantity', required=True)
    minimum_quantity = fields.Float(string='Minimum Required Quantity', default=10)
    status = fields.Selection([('sufficient', 'Sufficient'), ('low', 'Low')], string='Stock Status', compute='_compute_stock_status', store=True)

    @api.depends('stock_quantity', 'minimum_quantity')
    def _compute_stock_status(self):
        for inventory in self:
            if inventory.stock_quantity < inventory.minimum_quantity:
                inventory.status = 'low'
            else:
                inventory.status = 'sufficient'
