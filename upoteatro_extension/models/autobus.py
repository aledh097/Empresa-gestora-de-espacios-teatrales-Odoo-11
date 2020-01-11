# -*- coding: utf-8 -*-

from odoo import models, fields, api

class autobus(models.Model):
    _name = 'upoteatro_extension.autobus'
    _rec_name = 'matricula'

    matricula = fields.Char('Matricula', size=20, required=True)
    capacidad =  fields.Integer('Capacidad',required=True)
    entradasGrupales = fields.One2many('upoteatro_extension.entradagrupal','autobus','Entradas')

    state = fields.Selection([('noPreparado','No Preparado'),('preparado','Preparado'),('enMarcha','Autobús en marcha'),('finTrayecto','Fin del trayecto')],'Estado',default='noPreparado')

    @api.one
    def btn_submit_to_preparado(self):
        self.write({'state':'preparado'})

    @api.one
    def btn_submit_to_enMarcha(self):
        self.write({'state':'enMarcha'})

    @api.one
    def btn_submit_to_finTrayecto(self):
        self.write({'state':'finTrayecto'})

    @api.one
    def btn_submit_to_noPreparado(self):
        self.write({'state':'noPreparado'})

    def desasociarEntradas(self):
    	# Si un autobús se avería debemos de desvincular sus entradas grupales asociadas.
    	self.write({'entradasGrupales':[(5,)]})
