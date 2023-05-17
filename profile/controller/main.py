from odoo import http, api
from odoo.http import request


class MyDashboard(http.Controller):
    @http.route('/my/dashboard', type='http', auth='public', website=True)
    def render_dash_board(self):
        categories = request.env['link.categories'].sudo().search([])
        vals = {'categories': categories}
        return request.render("profile.portal_my_dashboard", vals)
