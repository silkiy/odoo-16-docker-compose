from odoo import models, fields

class Kelas(models.Model):
    _name = 'kelas'
    _description = 'Kelas'

    name = fields.Char(string='Nama', required=True)
    jenjang = fields.Selection([('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], string='Jenjang', required=True)
    jurusan_id = fields.Many2one('jurusan', string='Jurusan')