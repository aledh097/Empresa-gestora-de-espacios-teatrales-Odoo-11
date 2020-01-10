# -*- coding: utf-8 -*-

from odoo import models, fields, api

class entrada(models.Model):
	_inherit = 'upoteatro.entrada'

	entradaIndividual_id = fields.Many2one('upoteatro_extension.entradaindividual',string='Entrada Individual')
	entradaGrupal_id = fields.Many2one('upoteatro_extension.entradagrupal',string='Entrada Grupal')

	@api.one
	@api.constrains('butacas_ids','entradaIndividual_id','entradaGrupal_id')
	def _check_tipo_Entrada(self):
		if len(self.butacas_ids) > 1 and len(self.entradaIndividual_id)==1:
			raise models.ValidationError('No puede asignar una entrada individual a una entrada que ha comprado varias butacas.')
		elif len(self.butacas_ids) == 1 and len(self.entradaGrupal_id)==1:
			raise models.ValidationError('No puede asignar una entrada grupal a una entrada que ha comprado una sola butaca.')
