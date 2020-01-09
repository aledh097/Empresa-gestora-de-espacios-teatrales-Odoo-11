# -*- coding: utf-8 -*-

from odoo import models, fields, api

precioBaseTicket = 30

class entrada(models.Model):
    _name = 'upoteatro.entrada'
    _rec_name = 'representacion_id'

    haEntrado = fields.Boolean ('Ha entrado',required=True, default=False)
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