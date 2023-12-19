from odoo import models, fields

class Logs(models.Model):
    _name = 'logs.logs'
    logs_id = fields.Many2one("diagizilla.diagizilla")
    massage = fields.Text()

    