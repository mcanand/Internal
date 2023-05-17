from odoo import fields, models


class LinkCategory(models.Model):
    _name = 'link.categories'
    _description = 'Link Category'

    name = fields.Char(string='Link Categories', required=True)
    parent_id = fields.Many2one('link.categories')
