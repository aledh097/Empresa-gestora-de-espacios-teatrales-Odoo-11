# -*- coding: utf-8 -*-

from odoo import models, fields, api

class entradaindividual(models.Model):
    _name = 'upoteatro_extension.entradagrupal'
    _rec_name = 'numeroPersonas'
    
    numeroPersonas = fields.Integer('Número de personas',required=True)
    autobus = fields.Many2one('upoteatro_extension.autobus',string='Autobús')