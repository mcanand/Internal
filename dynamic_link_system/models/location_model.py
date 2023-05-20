from odoo import fields, models, api


class LocationCategories(models.Model):
    _name = 'location.categories'

    name = fields.Char(string="Category")