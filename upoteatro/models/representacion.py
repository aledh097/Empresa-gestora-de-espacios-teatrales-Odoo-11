# -*- coding: utf-8 -*-

from odoo import models, fields, api

class representacion(models.Model):
    _name = 'upoteatro.representacion'
    _rec_name = 'espectaculo_id'
    
    fechaHoraInicio = fields.Datetime('Hora Inicio',required=True, autodate = True)
    fechaHoraFin = fields.Datetime('Hora Fin',required=True, autodate = True)
    esAdaptada = fields.Boolean ('Representación Adaptada',required=True, default=False)
    espectaculo_id = fields.Many2one('upoteatro.espectaculo',string='Espectáculo',required=True)
    interpretes_ids = fields.Many2many('upoteatro.interprete',string='Intérpretes')
    teatro_id = fields.Many2one('upoteatro.teatro',string='Teatro') #De momento el required=True lo omitimos para que no de error en la carga de datos de la entrega 2.
    entradas_ids = fields.One2many('upoteatro.entrada','representacion_id','Entradas')
    
    @api.multi
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, "%s (%s)" % (record.espectaculo_id.name, record.fechaHoraInicio)))
        return res