# -*- coding: utf-8 -*-
# from odoo import http


# class Diagizilla(http.Controller):
#     @http.route('/diagizilla/diagizilla', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/diagizilla/diagizilla/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('diagizilla.listing', {
#             'root': '/diagizilla/diagizilla',
#             'objects': http.request.env['diagizilla.diagizilla'].search([]),
#         })

#     @http.route('/diagizilla/diagizilla/objects/<model("diagizilla.diagizilla"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('diagizilla.object', {
#             'object': obj
#         })
