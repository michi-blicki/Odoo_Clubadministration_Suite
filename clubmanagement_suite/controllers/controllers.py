# -*- coding: utf-8 -*-
# from odoo import http


# class ClubmanagementSuite(http.Controller):
#     @http.route('/clubmanagement_suite/clubmanagement_suite', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clubmanagement_suite/clubmanagement_suite/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('clubmanagement_suite.listing', {
#             'root': '/clubmanagement_suite/clubmanagement_suite',
#             'objects': http.request.env['clubmanagement_suite.clubmanagement_suite'].search([]),
#         })

#     @http.route('/clubmanagement_suite/clubmanagement_suite/objects/<model("clubmanagement_suite.clubmanagement_suite"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clubmanagement_suite.object', {
#             'object': obj
#         })

