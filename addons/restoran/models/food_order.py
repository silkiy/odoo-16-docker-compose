from odoo import models, fields, api

class FoodOrder(models.Model):
    _name = 'restaurant.food.order'
    _description = 'Food Order'

    table_id = fields.Many2one('restaurant.table.reservation', string='Table', required=True)
    order_time = fields.Datetime(string='Order Time', default=fields.Datetime.now)
    menu_item_ids = fields.Many2many('restaurant.menu.item', string='Menu Items')
    total_price = fields.Float(string='Total Price', compute='_compute_total_price', store=True)
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('served', 'Served')], default='draft', string='Status')

    @api.depends('menu_item_ids')
    def _compute_total_price(self):
        for order in self:
            order.total_price = sum(item.price for item in order.menu_item_ids)

    def action_confirm_order(self):
        self.state = 'confirmed'

    def action_serve_order(self):
        self.state = 'served'
