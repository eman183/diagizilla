# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class diagizilla(models.Model):
    _name = 'diagizilla.diagizilla'
    _description = 'diagizilla.diagizilla'
    name = fields.Char(string='Name',required=True)
    gender = fields.Selection([ ('female', 'Female'),('male', 'Male'),('other', 'Other')], string="Gender")
    country = fields.Many2one('res.country', string='Country')
    join_date = fields.Date(
            'Date', required=True,
            default=datetime.today())
    # best practice for called m2m realation is name_ids
    # we return more than one value so that we use m2m relation
    customers_ids = fields.Many2many('res.partner', string='Customers')
    tag_ids = fields.Many2many('crm.tag', string='Tags')
    # best practice for called m2m realation is name_id
    # we return one value so that we use m21 relation
    company_id = fields.Many2one('res.company', string='Company',required=True)
    notes = fields.Text(string='Notes')
    comments = fields.Char(string='Comments')
    logs = fields.One2many(comodel_name="logs.logs", inverse_name="logs_id")
    
 




    @api.onchange('name', 'gender', 'country', 'join_date','customers_ids','tag_ids','company_id','notes', 'comments' )
    def onchange_any_field(self):
        vals = {
                'massage': 'change happened at least in one field',
                'logs_id': self.id
            }

        self.env['logs.logs'].create(vals)