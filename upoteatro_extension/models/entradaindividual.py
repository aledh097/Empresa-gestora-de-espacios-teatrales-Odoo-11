# -*- coding: utf-8 -*-

from odoo import models, fields, api

class entradaindividual(models.Model):
    _name = 'upoteatro_extension.entradaindividual'
    _rec_name = 'entrada_id'

    tipoEntrada = fields.Selection([('juvenil','Juvenil'),
                                     ('jubilado','Jubilado'),
                                     ('infantil','Infantil'),
                                     ('estudiante','Estudiante'),
                                     ('normal','Normal'),],'Tipo de Entrada',required=True)
    entrada_id = fields.Many2one('upoteatro.entrada',string='Entrada',readonly=True)