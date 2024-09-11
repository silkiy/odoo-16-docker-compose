from odoo import models, fields, api

class TableReservation(models.Model):
    _name = 'restaurant.table.reservation'
    _description = 'Table Reservation'

    table_number = fields.Char(string='Table Number', required=True)
    customer_name = fields.Char(string='Customer Name', required=True)
    reservation_time = fields.Datetime(string='Reservation Time', required=True)
    guests = fields.Integer(string='Number of Guests', required=True)
    status = fields.Selection([('reserved', 'Reserved'), ('seated', 'Seated'), ('cancelled', 'Cancelled')], default='reserved', string='Status')

    def action_seat_customer(self):
        self.status = 'seated'

    def action_cancel_reservation(self):
        self.status = 'cancelled'
