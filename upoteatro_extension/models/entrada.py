# -*- coding: utf-8 -*-

from odoo import models, fields, api

class entrada(models.Model):
	_inherit = 'upoteatro.entrada'

	entradaIndividual_id = fields.Many2one('upoteatro_extension.entradaindividual',string='Entrada Individual')
	entradaGrupal_id = fields.Many2one('upoteatro_extension.entradagrupal',string='Entrada Grupal')