# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'
    
    isFCTPartner = fields.Boolean(string="FCTPartner", default=False)
    
    fctpPupils= fields.One2many('res.users',string="Pupils")
    
 