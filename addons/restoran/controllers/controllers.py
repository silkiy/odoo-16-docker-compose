# -*- coding: utf-8 -*-
# from odoo import http


# class Restoran(http.Controller):
#     @http.route('/restoran/restoran', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restoran/restoran/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('restoran.listing', {
#             'root': '/restoran/restoran',
#             'objects': http.request.env['restoran.restoran'].search([]),
#         })

#     @http.route('/restoran/restoran/objects/<model("restoran.restoran"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restoran.object', {
#             'object': obj
#         })
