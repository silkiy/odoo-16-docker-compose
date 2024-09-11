from odoo import models, fields, api

class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Course'


    name = fields.Char(string='Course Name', required=True)
    description = fields.Text(string='Description')
    user_id = fields.Many2one(comodel_name='res.users', string='Penanggung Jawab')
    session_line = fields.One2many(comodel_name='training.session', inverse_name='course_id', string='Sessions')
    instruktur_id = fields.Many2one(comodel_name='res.partner', string='Instruktur')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
    ], string='Status', default='draft', tracking=True)


class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Session'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Session Name', required=True, tracking=True) 
    course_id = fields.Many2one(comodel_name='training.course', string='Course Name', required=True, ondelete='cascade', tracking=True)
    start_date = fields.Date(string='Start Date', required=True , tracking=True)
    duration = fields.Float(string='Duration', required=True, tracking=True)
    seats = fields.Integer(string='Seats', required=True, tracking=True)
    peserta_ids = fields.Many2many(comodel_name='peserta', string='Peserta', tracking=True)
    instruktur_id = fields.Many2one(comodel_name='res.partner', string='Instruktur', tracking=True)

    
    
    no_hp = fields.Char(string='No HP', related='instruktur_id.mobile', tracking=True)
    email = fields.Char(string='Email', related='instruktur_id.email', tracking=True)
    jenis_kelamin = fields.Selection(related='instruktur_id.jenis_kelamin', tracking=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
    ], string='Status', default='draft', tracking=True)


    jml_peserta = fields.Integer(string='Jumlah Peserta', compute='_compute_jml_peserta', tracking=True)

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
