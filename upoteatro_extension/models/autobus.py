# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autobus(models.Model):
    _name = 'upoteatro_extension.autobus'
    _rec_name = 'matricula'

    matricula = fields.Char('Matricula', size=20, required=True)
    capacidad =  fields.Integer('Capacidad',required=True)
    entradasGrupales = fields.One2many('upoteatro_extension.entradagrupal','autobus','Entradas')