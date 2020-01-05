# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class empresa-gestora-de-espacios-teatrales-odoo-11__extension(models.Model):
#     _name = 'empresa-gestora-de-espacios-teatrales-odoo-11__extension.empresa-gestora-de-espacios-teatrales-odoo-11__extension'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100