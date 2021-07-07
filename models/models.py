# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime


class akssaleorder(models.Model):
     _inherit = 'sale.order'

     
     aks_newname = fields.Char('Order')

     @api.model_create_multi
     def create(self, vals):
          print("This is debugging on my sale_inhrit module>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
          print(vals)
          val_dict = vals and vals[0]
          val_dict['signed_by'] ='shani'
          val_dict['signed_on'] = datetime.now()
          val_dict['aks_newname'] ='first order'
          return super(akssaleorder, self).create(vals)