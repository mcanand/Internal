from odoo import fields, models


class Districts(models.Model):
    _name = 'res.country.state.district'
    _description = 'districts of state'

    name = fields.Char(string="District Name", required=True)
    code = fields.Char(string="District Code", required=True)
    state_id = fields.Many2one('res.country.state', string="State",
                               required=True)
    municipality_ids = fields.One2many('res.country.state.district.municipality', 'district_id')
    corporation_ids = fields.One2many('res.country.state.district.corporation', 'district_id')
    panchayat_ids = fields.One2many('res.country.state.district.panchayat', 'district_id')
