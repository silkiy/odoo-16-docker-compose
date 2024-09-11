from odoo import models, fields

class MenuItem(models.Model):
    _name = 'restaurant.menu.item'
    _description = 'Menu Item'

    name = fields.Char(string='Dish Name', required=True)
    price = fields.Float(string='Price', required=True)
    category = fields.Selection([('starter', 'Starter'), ('main_course', 'Main Course'), ('dessert', 'Dessert'), ('drink', 'Drink')], string='Category')
    ingredients = fields.Text(string='Ingredients')
    available = fields.Boolean(string='Available', default=True)
