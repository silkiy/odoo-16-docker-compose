from odoo import models, fields

class GuruKaryawan(models.Model):
    _name = 'guru.karyawan'
    _description = 'Guru dan Karyawan'

    name = fields.Char(string="Nama", required=True)
    nip = fields.Char(string="NIP", required=True)
    jenis_kelamin = fields.Selection([
        ('laki', 'Laki-laki'),
        ('perempuan', 'Perempuan')
    ], string="Jenis Kelamin", required=True)
    tempat_lahir = fields.Char(string="Tempat Lahir")
    tanggal_lahir = fields.Date(string="Tanggal Lahir")
    alamat = fields.Text(string="Alamat")
    no_hp = fields.Char(string="No HP")
    email = fields.Char(string="Email")
    jenis_pegawai = fields.Selection([
        ('guru', 'Guru'),
        ('karyawan', 'Karyawan')
    ], string="Jenis Pegawai", required=True)
