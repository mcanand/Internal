from odoo import http, api
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class MyDashboard(CustomerPortal):
    @http.route(['/my/dashboard', '/my/dashboard/<int:category_id>'], type='http', auth='user', website=True,
                methods=['GET', 'POST'])
    def render_dash_board(self, **kw):
        user = request.env.user
        available_links = user.partner_id.membership_type_id.external_web_link_ids
        categories = request.env['link.categories'].sudo().search([])
        if request.httprequest.method == 'POST':
            links = available_links.filtered_domain([('name', 'ilike', kw.get('search'))])
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
            links = available_links.filtered_domain([('link_category_id', '=', kw.get('category_id'))])
            rem = available_links.filtered_domain([('link_category_id.parent_id', '=', kw.get('category_id'))])
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

    @http.route(['/my/membership'], type='http', auth='user', website=True, methods=['GET', 'POST'])
    def render_membership_plans(self, **kw):
        values = self._prepare_portal_layout_values()
        user = request.env.user
        membership_types = self.get_member_ship_types()
        types = filter(lambda x: x.id != user.partner_id.membership_type_id.id, membership_types)
        values['types'] = types
        return request.render('profile.portal_my_membership_upgrade', values, headers={
            'X-Frame-Options': 'SAMEORIGIN',
            'Content-Security-Policy': "frame-ancestors 'self'"
        })

    def get_member_ship_types(self):
        return request.env['membership.types'].search([])

    @http.route(['/my/location/details'], type='http', auth='user', website=True,
                methods=['GET', 'POST'])
    def render_my_location_details(self, **kw):
        return request.render('profile.my_location_details')