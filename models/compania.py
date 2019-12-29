# -*- coding: utf-8 -*-

from odoo import models, fields, api

class compania(models.Model):
    _name = 'upoteatro.compania'
    
    CIF = fields.Char('CIF',size=32,required=True)
    name = fields.Char('Nombre', size=64, required=True)
    director = fields.Char('Director', size=64)
    espectaculos_ids = fields.Many2many('upoteatro.espectaculo',string='Espectáculos')
