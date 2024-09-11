from odoo import models, fields

class Jurusan(models.Model):
    _name = 'jurusan'
    _description = 'Jurusan'

    name = fields.Char(string='Nama Jurusan', required=True)
    deskripsi = fields.Text(string='Deskripsi')
    kelas_ids = fields.One2many('kelas', 'jurusan_id', string='Daftar Kelas')
