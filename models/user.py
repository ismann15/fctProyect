# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields, api, exceptions

class User (models.Model):
    _inherit = 'res.users'
    
    isPupil = fields.Boolean(string="Pupil", default = False)
    isTutor = fields.Boolean(string="Tutor", default = False)
    
    tutor = fields.Many2one('res.users',string="Tutor")
    pupils = fields.One2many('res.users','tutor',string = "Pupils")
    
    activities = fields.One2many('fctproyect.activity', 'owner', string="Activities")
    
    
    #partner = fields.Many2one('res.partner', ondelete='cascade', string="FCTPartner")
    
    @api.constrains('isPupil', 'isTutor')
    def _chech_not_pupil_and_tutor(self):
        if self.isPupil and self.isTutor:
            raise exceptions.ValidationError("User can be pupil and tutor at the same time")
    


#@api.onchange('isPupil', 'isTutor')
#def _chech_not_pupil_and_tutor(self):
#    if self.isPupil and self.isTutor == True:
#        return {
#                'warning': {
#                    'title': "Incorrect 'seats' value",
#                   'message': "The number of available seats may not be negative",
#                },
#               
#                
#        }
#        self.isPupil = False
#        self.isTutor = False  
# ondelete='set null', string="FCTPartner",index=True,domain=[('isPupil', '=', True)]
            
            
        
