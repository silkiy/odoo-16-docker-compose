from odoo import models, fields

class Ekstrakurikuler(models.Model):
    _name = 'ekstrakurikuler'
    _description = 'Ekstrakurikuler'

    name = fields.Char(string="Nama Ekstrakurikuler", required=True)
    deskripsi = fields.Text(string="Deskripsi")
    pembina_id = fields.Many2one('guru.karyawan', string="Pembina")
