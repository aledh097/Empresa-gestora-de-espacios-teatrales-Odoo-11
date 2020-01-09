# -*- coding: utf-8 -*-

from odoo import models, fields, api

class entradaindividual(models.Model):
    _name = 'upoteatro_extension.entradagrupal'
    _rec_name = 'autobus'
    
    numeroPersonas = fields.Integer('Número de personas',required=True)
    autobus = fields.Many2one('upoteatro_extension.autobus',string='Autobús')

    @api.multi
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, "Nº Personas: %s (Autobús: %s)" % (record.numeroPersonas, record.autobus.matricula)))
        return res