# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from odoo import models, fields, api, exceptions


class Activity (models.Model):
    _name ="fctproyect.activity"
    
    date = fields.Date (default=fields.Date.today)
    description = fields.Text(string = "Description")
    duration = fields.Float (string = "Duration")
    remarks = fields.Char (string ="Remarks")
    
    owner= fields.Many2one('res.users',string="Pupil",default=lambda self: self.env.user,readonly=True)
    
    @api.constrains('duration')
    def _check_duration(self):
        for r in self:
            if (0< r.duration > 8):
                raise exceptions.ValidationError("Duration cant be more than 8 hours or less than 0 hours")
            
    @api.constrains('duration')
    def _check_duration_by_day(self):
        duration_today=0
        for activity in self.search([('date','=',self.date),('owner','=',self.owner.id)]):
            duration_today=duration_today+activity.duration
            if activity.duration > 8:
                raise exceptions.ValidationError("You cant make more than 8 hours per day")
                
    @api.constrains('duration')
    def _check_total_duraction(self):
        tot_duration=0
        for activity in self.search([('owner','=',self.owner.id)]):
            tot_duration=tot_duration + activity.duration
            if tot_duration > 350:
                raise exceptions.ValidationError("You cant make more than 350 hours ")
    
           
            
            
    
    
            
    
                
    