# -*- coding: utf-8 -*-

from odoo import models, fields, api

class entradaindividual(models.Model):
    _name = 'upoteatro_extension.entradaindividual'
    _rec_name = 'tipoEntrada'

    tipoEntrada = fields.Selection([('juvenil','Juvenil'),
                                     ('jubilado','Jubilado'),
                                     ('infantil','Infantil'),
                                     ('estudiante','Estudiante'),
                                     ('normal','Normal'),],'Tipo de Entrada',required=True)