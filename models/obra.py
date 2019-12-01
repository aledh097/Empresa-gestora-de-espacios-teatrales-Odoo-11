# -*- coding: utf-8 -*-

from odoo import models, fields, api

class obra(models.Model):
    _name = 'upoteatro.obra'
    
    name = fields.Char('Nombre', size=64, required=True)
    autor = fields.Char('Autor', size=64, required=True)
    espectaculos_ids = fields.Many2many('upoteatro.espectaculo',string='Espectáculos')