from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    district_id = fields.Many2one('res.country.state.district',
                                  string="District",
                                  domain="[('state_id','=?', state_id)]")
    municipality_id = fields.Many2one(
        'res.country.state.district.municipality',
        string="Municipality",
        domain="[('district_id','=?', district_id)]")
    corporation_id = fields.Many2one('res.country.state.district.corporation',
                                     string="Corporation",
                                     domain="[('district_id','=?', district_id)]")
    panchayat_id = fields.Many2one('res.country.state.district.panchayat',
                                   string="Panchayat",
                                   domain="[('district_id','=?', district_id)]")
