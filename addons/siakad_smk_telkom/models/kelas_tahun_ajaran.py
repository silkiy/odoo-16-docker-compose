from odoo import models, fields

class KelasTahunAjaran(models.Model):
    _name = 'kelas.tahun.ajaran'
    _description = 'Kelas Tahun Ajaran'

    name = fields.Char(string="Nama", required=True)
    siswa_ids = fields.One2many('siswa', 'name', string="Daftar Siswa")
    wali_kelas_id = fields.Many2one('guru.karyawan', string="Wali Kelas")
