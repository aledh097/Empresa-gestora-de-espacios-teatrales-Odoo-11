# -*- coding: utf-8 -*-

from odoo import models, fields, api

class espectaculo(models.Model):
    _name = 'upoteatro.espectaculo'

    name = fields.Char('Nombre', size=64, required=True)
    productor = fields.Char('Productor', size=64)
    categoria = fields.Selection([('teatro clásico','Teatro Clásico'),
                                     ('teatro contemporáneo','Teatro Contemporáneo‎'),
                                     ('teatro infantil','Teatro Infantil‎'),
                                     ('musical','Musical'),
                                     ('concierto‎‎','Concierto‎'),
                                     ('evento humorístico‎','‎Evento humorísticos'),
                                     ('ilusionismo','Ilusionismo'),],
                                     'Categoría')
    gastos = fields.Float('Gastos')
    representacion_ids = fields.One2many('upoteatro.representacion','espectaculo_id','Representaciones')
    obras_ids = fields.Many2many('upoteatro.obra',string='Obras')
    companias_ids = fields.Many2many('upoteatro.compania',string='Compañías')
