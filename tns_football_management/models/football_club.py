from odoo import fields, models


class FootballClub(models.Model):
    _name = 'football.club'
    _description = 'Football Club'
    
    name = fields.Char(string='Name', required=True)
