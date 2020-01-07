# -*- coding: utf-8 -*-

from odoo import models, fields, api

class teatro(models.Model):
    _name = 'upoteatro.teatro'

    name = fields.Char('Nombre', size=64, required=True)
    direccion = fields.Char('Dirección', size=64)
    aforo = fields.Integer('Aforo', required=True)
    representaciones_ids = fields.One2many('upoteatro.representacion','teatro_id','Representaciones')
    butacas_ids = fields.One2many('upoteatro.butaca','teatro_id','Butacas')