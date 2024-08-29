from odoo import models, fields, api

class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Course'

    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    user_id = fields.Many2one(comodel_name='res.users', string='Penanggung Jawab')
    session_line = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Sessions')
    instruktur_id = fields.Many2one(comodel_name='res.partner', string='Instruktur')

class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Session'

    name = fields.Char(string='Session Name', required=True)
    course_id = fields.Many2one(comodel_name='training.course', string='Course Name', required=True, ondelete='cascade')
    start_date = fields.Date(string='Start Date', required=True)
    duration = fields.Float(string='Duration', required=True)
    seats = fields.Integer(string='Seats', required=True)
    peserta_ids = fields.Many2many(comodel_name='peserta', string='Peserta')
    instruktur_id = fields.Many2one(comodel_name='res.partner', string='Instruktur')
    
    no_hp = fields.Char(string='No HP', related='instruktur_id.mobile')
    email = fields.Char(string='Email', related='instruktur_id.email')
    jenis_kelamin = fields.Selection(related='instruktur_id.jenis_kelamin')

    state = fields.Selection(string='Status', selection=[('draft', 'Draft'), ('confirm', 'Sedang Berlangsung'), ('done', 'Selesai')], default='draft', tracking=True)

    jml_peserta = fields.Integer(string='Jumlah Peserta', compute='_compute_jml_peserta')

    @api.depends('peserta_ids')
    def _compute_jml_peserta(self):
        for record in self:
            record.jml_peserta = len(record.peserta_ids)

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'
