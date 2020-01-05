# -*- coding: utf-8 -*-
from odoo import http

# class Empresa-gestora-de-espacios-teatrales-odoo-11Extension(http.Controller):
#     @http.route('/empresa-gestora-de-espacios-teatrales-odoo-11__extension/empresa-gestora-de-espacios-teatrales-odoo-11__extension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empresa-gestora-de-espacios-teatrales-odoo-11__extension/empresa-gestora-de-espacios-teatrales-odoo-11__extension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('empresa-gestora-de-espacios-teatrales-odoo-11__extension.listing', {
#             'root': '/empresa-gestora-de-espacios-teatrales-odoo-11__extension/empresa-gestora-de-espacios-teatrales-odoo-11__extension',
#             'objects': http.request.env['empresa-gestora-de-espacios-teatrales-odoo-11__extension.empresa-gestora-de-espacios-teatrales-odoo-11__extension'].search([]),
#         })

#     @http.route('/empresa-gestora-de-espacios-teatrales-odoo-11__extension/empresa-gestora-de-espacios-teatrales-odoo-11__extension/objects/<model("empresa-gestora-de-espacios-teatrales-odoo-11__extension.empresa-gestora-de-espacios-teatrales-odoo-11__extension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empresa-gestora-de-espacios-teatrales-odoo-11__extension.object', {
#             'object': obj
#         })