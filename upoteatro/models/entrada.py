# -*- coding: utf-8 -*-

from odoo import models, fields, api

#import logging

#_logger = logging.getLogger(__name__)
    

class entrada(models.Model):
    _name = 'upoteatro.entrada'
    _rec_name = 'representacion_id'

    esAdaptada = fields.Boolean('Es adaptada',required=True)
    precio = fields.Float('Precio total', required=True)
    precioConDescuento = fields.Float(compute='_calcularPrecio', string='Precio total con descuento', store=True)
    representacion_id = fields.Many2one('upoteatro.representacion',string='Representación',required=True)
    porcentajeDescuento = fields.Integer('% de descuento',required=True, default=0)
    butacas_ids = fields.Many2many('upoteatro.butaca',string='Butacas')

    @api.one
    @api.depends('precio','precioConDescuento','porcentajeDescuento')
    def _calcularPrecio(self):
    	self.precioConDescuento = (1-(self.porcentajeDescuento/100))*self.precio

    @api.onchange('porcentajeDescuento')
    def onchange_porcentajeDescuento(self):
    	resultado = {}
    	if self.porcentajeDescuento > 100:
    		resultado = {'value': {'porcentajeDescuento': 100},
    		'warning': {'title': 'Máximo 100%',
    					'message': 'El máximo de porcentaje de descuento es de 100%'}}
    	elif self.porcentajeDescuento < 0:
    		resultado = {'value': {'porcentajeDescuento': 0},
    		'warning': {'title': 'Mínimo 0%',
    					'message': 'El mínimo de porcentaje de descuento es de 0%'}}
    	return resultado

    @api.onchange('representacion_id')
    def _onchange_esAdaptada(self):
    	#_logger.debug("1- esAdaptada en entrada: " + str(self.esAdaptada) + " esAdaptada en representacion: " + str(self.representacion_id.esAdaptada))
    	if(self.esAdaptada==True) and (self.representacion_id.esAdaptada==False):
    		#_logger.debug("2- esAdaptada en entrada: " + str(self.esAdaptada) + " esAdaptada en representacion: " + str(self.representacion_id.esAdaptada))
    		self.representacion_id.write({'esAdaptada':True})