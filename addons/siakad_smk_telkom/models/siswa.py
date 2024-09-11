from odoo import models, fields

class Siswa(models.Model):
    _name = 'siswa'
    _description = 'Siswa'

    name = fields.Char(string="Nama", required=True)

    nis = fields.Char(string="NIS", required=True)  
    
    jenis_kelamin = fields.Selection([('laki', 'Laki-laki'), ('perempuan', 'Perempuan')], string="Jenis Kelamin", required=True)
    tempat_lahir = fields.Char(string="Tempat Lahir")
    tanggal_lahir = fields.Date(string="Tanggal Lahir")
    alamat = fields.Text(string="Alamat")
    no_hp = fields.Char(string="No HP")
    email = fields.Char(string="Email")
    orangtua_id = fields.Many2one('orang.tua', string="Orangtua")

    # kelas_id = fields.Many2one('kelas.tahun.ajaran', string="Kelas Tahun Ajaran")
