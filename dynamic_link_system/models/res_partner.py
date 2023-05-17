from odoo import fields, models


class ResUsersInherit(models.Model):
    _inherit = 'res.partner'

    franchise = fields.Boolean(string='Franchise Member')
    member_type = fields.Selection([('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum')],
                                   default='silver',
                                   required=True,
                                   string='Membership Type')
