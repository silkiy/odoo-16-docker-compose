from odoo import models, fields

class TahunPelajaran(models.Model):
    _name = 'tahun.pelajaran'
    _description = 'Tahun Pelajaran'

    name = fields.Char(string='Nama Tahun Pelajaran', required=True)
    deskripsi = fields.Text(string='Deskripsi')
    is_active = fields.Boolean(string='Aktif', default=False)

    def write(self, vals):
        if 'is_active' in vals and vals['is_active']:
            
            self.env['tahun.pelajaran'].search([('is_active', '=', True)]).write({'is_active': False})
        return super(TahunPelajaran, self).write(vals)
