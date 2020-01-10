# -*- coding: utf-8 -*-

from odoo import models, fields, api
#import logging

#_logger = logging.getLogger(__name__)

class butaca(models.Model):
    _name = 'upoteatro.butaca'
    _rec_name = 'asiento'

    fila = fields.Integer('Fila',required=True)
    zona = fields.Selection([('platea','Platea'),('anfiteatro','Anfiteatro'),('paraiso','Paraíso'),
                             ('palco','Palco')],'Zona',required=True)
    asiento = fields.Integer('Asiento',required=True)
    teatro_id = fields.Many2one('upoteatro.teatro',string='Teatro',required=True)
    entradas_ids = fields.Many2many('upoteatro.entrada',string='Entradas')

    @api.one
    @api.constrains('teatro_id')
    def _check_num_butacas(self):
    	#_logger.debug("Numero de butacas: " + str(self.teatro_id.aforo) + " Numero de aforo: "  + str(len(self.teatro_id.butacas_ids)))
    	if(self.teatro_id.aforo < len(self.teatro_id.butacas_ids)):
    		raise models.ValidationError('No puede existir más butacas que en el aforo del teatro.')
