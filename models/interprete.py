# -*- coding: utf-8 -*-

from odoo import models, fields, api

class interprete(models.Model):
    _name = 'upoteatro.interprete'
    
    DNI = fields.Char('DNI', size=32, required=True)
    name = fields.Char('Nombre', size=32, required=True)
    apellidos = fields.Char('Apellidos', size=32, required=True)
    representaciones_ids = fields.Many2many('upoteatro.representacion',string='Representaciones')
    idiomas_ids = fields.Many2many('upoteatro.idioma',string='Idiomas')