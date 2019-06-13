# -*- coding: utf-8 -*-
from odoo import http

# class WebBibov1(http.Controller):
#     @http.route('/web_bibov1/web_bibov1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_bibov1/web_bibov1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_bibov1.listing', {
#             'root': '/web_bibov1/web_bibov1',
#             'objects': http.request.env['web_bibov1.web_bibov1'].search([]),
#         })

#     @http.route('/web_bibov1/web_bibov1/objects/<model("web_bibov1.web_bibov1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_bibov1.object', {
#             'object': obj
#         })