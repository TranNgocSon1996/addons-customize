from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    club_id = fields.Many2one('football.club', string="Football Club")
