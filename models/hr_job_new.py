from odoo import models, fields, api
from datetime import datetime

class HrJob(models.Model):
    _inherit = 'hr.job'

    tarih_son = fields.Datetime("Son Tarih")


    def _check_tarih_son(self):
        # Şu anki tarih ve saat
        now = datetime.now()

        # Tarih_son dolu ve geçmişse website_published alanını False yap
        jobs = self.search([('tarih_son', '!=', False), ('tarih_son', '<=', now), ('website_published', '=', True)])
        for job in jobs:
            job.website_published = False

    def clear_tarih_son(self):
        """ Bu işlev tarih_son alanını temizlemek için kullanılır """
        self.tarih_son = False
