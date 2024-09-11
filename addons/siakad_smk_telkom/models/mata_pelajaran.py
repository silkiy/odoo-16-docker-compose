from odoo import models, fields

class MataPelajaran(models.Model):
    _name = 'mata.pelajaran'
    _description = 'Mata Pelajaran'

    name = fields.Char(string="Nama Mata Pelajaran", required=True)
    jadwal_pelajaran = fields.Char(string="Jadwal Pelajaran")
