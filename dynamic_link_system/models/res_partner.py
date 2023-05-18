from odoo import fields, models


class ResUsersInherit(models.Model):
    _inherit = 'res.partner'

    franchise = fields.Boolean(string='Franchise Member')
    #TODO Delete member_type field dont need
    member_type = fields.Selection([('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum')],
                                   default='silver',
                                   string='Membership Type')
    membership_type_id = fields.Many2one('membership.types')
