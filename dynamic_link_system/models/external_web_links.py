from odoo import models, fields


class ExternalWebLinks(models.Model):
    _name = 'external.web.links'
    _description = 'External Web Links'

    name = fields.Char(string='Name', required=True)
    link = fields.Char(string='Link', required=True)
    link_category_id = fields.Many2one('link.categories', string='Link Category', required=True)
