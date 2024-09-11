from odoo import models, fields, api



class Hobby(models.Model):
    _name = 'hobby'
    _description = 'Hobby'

    name = fields.Char(string='Nama Hobby', required=True)
    ket = fields.Text(string='Keterangan')
    active = fields.Boolean(string='active', default=True)
