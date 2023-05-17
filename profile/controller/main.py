from odoo import http, api
from odoo.http import request


class MyDashboard(http.Controller):
    @http.route(['/my/dashboard', '/my/dashboard/<int:category_id>'], type='http', auth='user', website=True, methods=['GET', 'POST'])
    def render_dash_board(self, **kw):
        categories = request.env['link.categories'].sudo().search([])
        if request.httprequest.method == 'POST':
            links = request.env['external.web.links'].sudo().search([('name', 'ilike', kw.get('search'))])
            vals = {'categories': categories,
                    'category_id': 0,
                    'name': 'Search',
                    'links': links,
                    'search': kw.get('search')}
            return request.render("profile.external_links", vals, headers={
                'X-Frame-Options': 'SAMEORIGIN',
                'Content-Security-Policy': "frame-ancestors 'self'"
            })
        vals = {'categories': categories,
                'category_id': categories[0].id if categories else '',
                'name': categories[0].name.title() if categories else 'No Records Yet'}
        if kw.get('category_id'):
            links = request.env['external.web.links'].sudo().search([('link_category_id', '=', kw.get('category_id'))])
            rem = request.env['external.web.links'].sudo().search(
                [('link_category_id.parent_id', '=', kw.get('category_id'))])
            vals.update({'links': links + rem if rem else links,
                         'category_id': kw.get('category_id'),
                         'name': self.get_category(kw.get('category_id')).name.title()})
            return request.render("profile.external_links", vals, headers={
                'X-Frame-Options': 'SAMEORIGIN',
                'Content-Security-Policy': "frame-ancestors 'self'"
            })
        if vals.get('category_id'):
            return request.redirect('/my/dashboard/%s' % vals.get('category_id'))
        return request.render("profile.portal_my_dashboard", vals)

    def get_category(self, category_id):
        return request.env['link.categories'].sudo().browse(category_id)