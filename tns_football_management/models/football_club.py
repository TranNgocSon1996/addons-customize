from odoo import fields, models, api


class FootballClub(models.Model):
    _name = 'football.club'
    _inherit = 'image.mixin'
    _order = 'id'
    _description = 'Football Club'
    
    name = fields.Char(string='Name', required=True)
    nickname = fields.Char(string='Nickname')
    coach_id = fields.Many2one('res.partner', string='Coach')
    captain_id = fields.Many2one('res.partner', string='Captain', required=True)
    player_total = fields.Integer(string='Player Total', compute='_compute_player_total', stored=True, default=0)
    player_ids = fields.One2many('res.partner', inverse_name='club_id', string="Player")
    
    @api.depends('player_ids')
    def _compute_player_total(self):
        for r in self:
            r.player_total = len(r.player_ids)
