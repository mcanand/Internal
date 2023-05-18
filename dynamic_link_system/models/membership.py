from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class Membership(models.Model):
    _name = 'membership.types'
    _description = 'membership type'

    name = fields.Char(string='Membership Name', required=True)
    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(string="Price",
                              compute='_compute_price',
                              readonly=False,
                              store=True)
    external_web_lik_ids = fields.Many2many('external.web.links', string='Web Links')
    members_count = fields.Integer(compute='_compute_members_count')

    @api.depends('members_count')
    def _compute_members_count(self):
        for rec in self:
            count = len(self.env['res.partner'].search([('membership_type_id', '=', rec.id)]))
            rec.members_count = count

    @api.depends('product_id')
    def _compute_price(self):
        for rec in self:
            rec.price_unit = rec.product_id.lst_price

    @api.onchange('price_unit')
    def onchange_price_unit(self):
        for rec in self:
            if rec.product_id:
                rec.product_id.write({'lst_price': rec.price_unit})
            else:
                raise ValidationError(_('Add a product first'))

    def action_show_members(self):
        ctx = dict(
            default_membership_type_id=self.id,
            default_franchise=True,
        )
        action = {
            "type": "ir.actions.act_window",
            "name": "Members",
            "res_model": "res.partner",
            "view_mode": "tree,kanban,form",
            "domain": [("membership_type_id", "=", self.id)],
            "context": ctx
        }
        return action
