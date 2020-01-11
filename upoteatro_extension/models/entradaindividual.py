# -*- coding: utf-8 -*-

from odoo import models, fields, api

class entradaindividual(models.Model):
    _name = 'upoteatro_extension.entradaindividual'
    _rec_name = 'tipoentrada'

    tipoentrada = fields.Selection([('juvenil','Juvenil'),
                                     ('jubilado','Jubilado'),
                                     ('infantil','Infantil'),
                                     ('estudiante','Estudiante'),
                                     ('normal','Normal'),],'Tipo de Entrada',required=True, store=True)

    _sql_constraints = [('entradaindividual_tipoentrada_unique', 'UNIQUE (tipoentrada)', 'El tipo de entrada debe ser único')]