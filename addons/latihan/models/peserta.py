from odoo import models, fields, api

class Peserta(models.Model):
    _name = 'peserta'
    _description = 'Tabel Peserta'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner ID', required=True, ondelete='cascade')
    tmp_lahir = fields.Char(string='Tempat Lahir')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    pendidikan = fields.Selection(string='Jenjang Pendidikan', selection=[('sd', 'SD'), ('smp', 'SMP'),('sma', 'SMA/SMK'), ('s1', 'Sarjana S1'),])
    pekerjaan = fields.Char(string='Pekerjaan')
    is_menikah = fields.Boolean(string='Sudah Menikah')
    nama_pasangan = fields.Char(string='Nama Pasangan')
    hp_pasangan = fields.Char(string='HP Pasangan')
    hobby_id = fields.Many2many(comodel_name='hobby', string='Hobby')
    

    no_peserta = fields.Char(string='No Peserta', readonly=True)

    @api.model
    def create(self, vals):
        vals['no_peserta'] = self.env['ir.sequence'].next_by_code('peserta')
        return super(Peserta, self).create(vals)

