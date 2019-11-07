# -*- coding: utf-8 -*-
from odoo import http

# class CustomeTicket(http.Controller):
#     @http.route('/custome_ticket/custome_ticket/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custome_ticket/custome_ticket/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custome_ticket.listing', {
#             'root': '/custome_ticket/custome_ticket',
#             'objects': http.request.env['custome_ticket.custome_ticket'].search([]),
#         })

#     @http.route('/custome_ticket/custome_ticket/objects/<model("custome_ticket.custome_ticket"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custome_ticket.object', {
#             'object': obj
#         })