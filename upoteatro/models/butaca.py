# -*- coding: utf-8 -*-

from odoo import models, fields, api

class butaca(models.Model):
    _name = 'upoteatro.butaca'
    _rec_name = 'asiento'

    fila = fields.Integer('Fila',required=True)
    zona = fields.Selection([('platea','Platea'),('anfiteatro','Anfiteatro'),('paraiso','Paraíso'),
                             ('palco','Palco')],'Zona',required=True)
    asiento = fields.Integer('Asiento',required=True)
    teatro_id = fields.Many2one('upoteatro.teatro',string='Teatro',required=True)
    entradas_ids = fields.Many2many('upoteatro.entrada',string='Entradas')