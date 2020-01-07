# -*- coding: utf-8 -*-

from odoo import models, fields, api

class entrada(models.Model):
    _name = 'upoteatro.entrada'
    _rec_name = 'representacion_id'

    haEntrado = fields.Boolean ('Ha entrado',required=True, default=False)
    esAdaptada = fields.Boolean('Es adaptada',required=True)
    precio = fields.Float('Precio',required=True)
    representacion_id = fields.Many2one('upoteatro.representacion',string='Representación',required=True)
    porcentajeDescuento = fields.Integer('% de descuento',required=True)
    butacas_ids = fields.Many2many('upoteatro.butaca',string='Butacas')