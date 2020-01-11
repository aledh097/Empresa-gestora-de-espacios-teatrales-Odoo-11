# -*- coding: utf-8 -*-

from odoo import models, fields, api

class representacion(models.Model):
    _name = 'upoteatro.representacion'
    _rec_name = 'espectaculo_id'
    
    fechahorainicio = fields.Datetime('Hora Inicio',required=True, autodate = True, store=True)
    fechahorafin = fields.Datetime('Hora Fin',required=True, autodate = True, store=True)
    esAdaptada = fields.Boolean ('Representación Adaptada',required=True, default=False)
    espectaculo_id = fields.Many2one('upoteatro.espectaculo',string='Espectáculo',required=True)
    interpretes_ids = fields.Many2many('upoteatro.interprete',string='Intérpretes')
    teatro_id = fields.Many2one('upoteatro.teatro',string='Teatro') #De momento el required=True lo omitimos para que no de error en la carga de datos de la entrega 2.
    entradas_ids = fields.One2many('upoteatro.entrada','representacion_id','Entradas')

    _sql_constraints = [('representacion_fechas_constraint', 'CHECK((fechahorainicio <= fechahorafin))', 'La hora de finalización debe ser posterior a la hora de inicio.')]
    
    @api.multi
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, "%s (%s)" % (record.espectaculo_id.name, record.fechahorainicio)))
        return res

    @api.one
    @api.constrains('esAdaptada','interpretes_ids')
    def _check_tiene_interprete(self):
        if(self.esAdaptada == True and len(self.interpretes_ids) == 0):
            raise models.ValidationError('Por favor añada un interprete de signos a la representación, ya que es adaptada.')
        elif(self.esAdaptada == False and len(self.interpretes_ids) > 0):
            raise models.ValidationError('Por favor no puede añadir un interprete de signos a una representación no adaptada.')