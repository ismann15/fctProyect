# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields, api, exceptions


class Activity (models.Model):
    _name ='fctproyect.activity'
    
    date = fields.Date (default=fields.Date.today)
    description = fields.Text(string = "Description")
    duration = fields.Float (string = "Duration")
    remarks = fields.Char (string ="Remarks")
    
    owner= fields.Many2one("res.users", ondelete="cascade", string="Owner", required=True, default=lambda self: self.env.user)
    
    @api.constrains('duration')
    def _check_duration(self):
        for t in self:
            if t.duration > 8:
                raise exceptions.ValidationError("Duration cant be more than 8 hours")
    
    
           
            
            
    
    
            
    
                
    