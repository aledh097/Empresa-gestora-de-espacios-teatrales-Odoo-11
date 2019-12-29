# -*- coding: utf-8 -*-

from odoo import models, fields, api

class idioma(models.Model):
    _name = 'upoteatro.idioma'
    
    name = fields.Char('Nombre', size=64, required=True)
    interpretes_ids = fields.Many2many('upoteatro.interprete',string='Intérpretes')
