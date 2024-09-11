from odoo import models, fields

class OrangTua(models.Model):
    _name = 'orang.tua'
    _description = 'Orang Tua'

    name = fields.Char(string="Nama", required=True)
    jenis_kelamin = fields.Selection([('laki', 'Laki-laki'), ('perempuan', 'Perempuan')], string="Jenis Kelamin", required=True)
    tempat_lahir = fields.Char(string="Tempat Lahir")
    tanggal_lahir = fields.Date(string="Tanggal Lahir")
    alamat = fields.Text(string="Alamat")
    no_hp = fields.Char(string="No HP")
    email = fields.Char(string="Email")
    anak_ids = fields.One2many('siswa', 'orangtua_id', string="Anak")