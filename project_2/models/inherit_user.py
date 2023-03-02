from odoo import api, fields, models

class res_users_ex(models.Model):
    _inherit = 'res.users'

    team_id = fields.Many2one('res.users' ,string='Team)