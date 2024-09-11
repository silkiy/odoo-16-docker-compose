from odoo import models, fields

class Organisasi(models.Model):
    _name = 'organisasi'
    _description = 'Organisasi'

    name = fields.Char(string="Nama Organisasi", required=True)
    deskripsi = fields.Text(string="Deskripsi")
    pembina_id = fields.Many2one('guru.karyawan', string="Pembina")
