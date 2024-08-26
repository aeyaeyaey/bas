from odoo import models, fields, api



class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    x_partner = fields.Many2one('res.partner', string="Related Partner", help="The partner related to this employee.")
    x_tck = fields.Char(related='x_partner.tc_kimlik_no', string="TC Kimlik No:", store =True)
    x_il = fields.Many2one(related='x_partner.il_id', string="İl",store=True)
    x_ilce = fields.Many2one(related='x_partner.ilce_id', string="İlçe:",store=True)
    x_adres = fields.Char(related='x_partner.adres', string="Adres:",store=True)
    x_b_date = fields.Date(related='x_partner.birth_date', string="Doğum Tarihi:",store=True)
    x_b_place = fields.Many2one(related='x_partner.birth_place', string="Doğum Yeri:",store=True)
    x_school_email = fields.Char(related='x_partner.school_email', string="Okul E-Maili:",store=True)
    x_twitter = fields.Char(related='x_partner.twitter_account', string="Twitter:",store=True)
    x_facebook = fields.Char(related='x_partner.facebook_account', string="Facebook:",store=True)
    x_instagram = fields.Char(related='x_partner.instagram_account', string="İnstagram:",store=True)
    x_linkedin = fields.Char(related='x_partner.linkedin_account', string="Linkedin:",store=True)
    x_uni = fields.Many2one(related='x_partner.uni_id', string="Üniversite:",store=True)
    x_fakulte = fields.Many2one(related='x_partner.fak_id', string="Fakülte:",store=True)
    x_bolum = fields.Many2one(related='x_partner.bolum_id', string="Bölüm:",store=True)
    x_nation = fields.Many2one(related='x_partner.nationality_id', string="Uyruk:",store=True)
    x_gender = fields.Selection([
        ('male', 'Erkek'),
        ('female', 'Kadın'),
    ],related='x_partner.gender', string='Cinsiyet')

    emp_tckimlikno = fields.Char("TC Kimlik No", compute='_compute_tckimlikno', store=True)
    emp_partner_il = fields.Char("İl  ", compute='_compute_city', store=True)
    emp_partner_ilce = fields.Char("İlçe", compute='_compute_district', store=True)
    emp_partner_lise = fields.Char("Lise", compute='_compute_highschool', store=True)
    emp_partner_adres = fields.Char("Adres", compute='_compute_address', store=True)
    emp_partner_birth_date = fields.Date("Doğum Günü", compute='_compute_birth_date', store=True)
    emp_partner_birth_place = fields.Char("Doğum Yeri", compute='_compute_birth_place', store=True)
    emp_partner_school_email = fields.Char("Okul Email", compute='_compute_school_email', store=True)
    emp_partner_twitter_account = fields.Char("Twitter", compute='_compute_twitter_account', store=True)
    emp_partner_facebook_account = fields.Char("Facebook", compute='_compute_facebook_account', store=True)
    emp_partner_instagram_account = fields.Char("Instagram", compute='_compute_instagram_account', store=True)
    emp_partner_linkedin_account = fields.Char("LinkedIn", compute='_compute_linkedin_account', store=True)
    emp_partner_uni = fields.Char("Üniversite", compute='_compute_uni', store=True)
    emp_partner_fak = fields.Char("Fakülte", compute='_compute_fak', store=True)
    emp_partner_bolum = fields.Char("Bölüm", compute='_compute_bolum', store=True)
    emp_partner_nationality = fields.Char("Uyruk", compute='_compute_nationality', store=True)
    emp_partner_tc_kimlik_no = fields.Char("Tc Kimlik No", compute='_compute_tc_kimlik_no', store=True)
    emp_partner_gender = fields.Selection([
        ('male', 'Erkek'),
        ('female', 'Kadın'),
    ], compute='_compute_gender', store=True)

    @api.depends('user_id', 'user_partner_id.tckimlikno')
    def _compute_tckimlikno(self):
        for record in self:
            record.emp_tckimlikno = record.user_id.partner_id.tckimlikno

    @api.depends('user_partner_id', 'user_partner_id.il_id')
    def _compute_city(self):
        for applicant in self:
            applicant.emp_partner_il = applicant.user_partner_id.il_id.name

    @api.depends('user_partner_id', 'user_partner_id.il_id')
    def _compute_city(self):
        for record in self:
            record.emp_partner_il = record.user_partner_id.il_id.name

    @api.depends('user_partner_id', 'user_partner_id.ilce_id')
    def _compute_district(self):
        for record in self:
            record.emp_partner_ilce = record.user_partner_id.ilce_id.name

    @api.depends('user_partner_id', 'user_partner_id.lise_id')
    def _compute_highschool(self):
        for record in self:
            record.emp_partner_lise = record.user_partner_id.lise_id.name

    @api.depends('user_partner_id', 'user_partner_id.adres')
    def _compute_address(self):
        for record in self:
            record.emp_partner_adres = record.user_partner_id.adres

    @api.depends('user_partner_id', 'user_partner_id.birth_date')
    def _compute_birth_date(self):
        for record in self:
            record.emp_partner_birth_date = record.user_partner_id.birth_date

    @api.depends('user_partner_id', 'user_partner_id.birth_place')
    def _compute_birth_place(self):
        for record in self:
            record.emp_partner_birth_place = record.user_partner_id.birth_place

    @api.depends('user_partner_id', 'user_partner_id.school_email')
    def _compute_school_email(self):
        for record in self:
            record.emp_partner_school_email = record.user_partner_id.school_email

    @api.depends('user_partner_id', 'user_partner_id.twitter_account')
    def _compute_twitter_account(self):
        for record in self:
            record.emp_partner_twitter_account = record.user_partner_id.twitter_account

    @api.depends('user_partner_id', 'user_partner_id.facebook_account')
    def _compute_facebook_account(self):
        for record in self:
            record.emp_partner_facebook_account = record.user_partner_id.facebook_account

    @api.depends('user_partner_id', 'user_partner_id.instagram_account')
    def _compute_instagram_account(self):
        for record in self:
            record.emp_partner_instagram_account = record.user_partner_id.instagram_account

    @api.depends('user_partner_id', 'user_partner_id.linkedin_account')
    def _compute_linkedin_account(self):
        for record in self:
            record.emp_partner_linkedin_account = record.user_partner_id.linkedin_account

    @api.depends('user_partner_id', 'user_partner_id.uni_id')
    def _compute_uni(self):
        for record in self:
            record.emp_partner_uni = record.user_partner_id.uni_id.name

    @api.depends('user_partner_id', 'user_partner_id.fak_id')
    def _compute_fak(self):
        for record in self:
            record.emp_partner_fak = record.user_partner_id.fak_id.name

    @api.depends('user_partner_id', 'user_partner_id.bolum_id')
    def _compute_bolum(self):
        for record in self:
            record.emp_partner_bolum = record.user_partner_id.bolum_id.name

    @api.depends('user_partner_id', 'user_partner_id.nationality_id')
    def _compute_nationality(self):
        for record in self:
            record.emp_partner_nationality = record.user_partner_id.nationality_id.name

    @api.depends('user_partner_id', 'user_partner_id.tc_kimlik_no')
    def _compute_tc_kimlik_no(self):
        for record in self:
            record.emp_partner_tc_kimlik_no = record.user_partner_id.tc_kimlik_no

    @api.depends('user_partner_id', 'user_partner_id.gender')
    def _compute_gender(self):
        for record in self:
            record.emp_partner_gender = record.user_partner_id.gender


