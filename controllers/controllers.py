# -*- coding: utf-8 -*-
from odoo import http

# class Fctproyect(http.Controller):
#     @http.route('/fctproyect/fctproyect/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fctproyect/fctproyect/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fctproyect.listing', {
#             'root': '/fctproyect/fctproyect',
#             'objects': http.request.env['fctproyect.fctproyect'].search([]),
#         })

#     @http.route('/fctproyect/fctproyect/objects/<model("fctproyect.fctproyect"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fctproyect.object', {
#             'object': obj
#         })