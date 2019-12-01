# -*- coding: utf-8 -*-

from odoo import models, fields, api

class representacion(models.Model):
    _name = 'upoteatro.representacion'

    fechaHoraInicio = fields.Datetime('Hora Inicio',required=True, autodate = True)
    fechaHoraFin = fields.Datetime('Hora Fin',required=True, autodate = True)
    esAdaptada = fields.Boolean ('Representación Adaptada',required=True, default=False)
    espectaculo_id = fields.Many2one('upoteatro.espectaculo',string = 'Espectáculo',required=True)
    interpretes_ids = fields.Many2many('upoteatro.interprete',string="Intérpretes",required=True)
