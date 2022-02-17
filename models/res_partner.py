# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):

    _inherit = "res.partner"


    experience_ids = fields.One2many(
        comodel_name='partner.experience',
        inverse_name='partner_id',
        string='Experience'
    )

    number_skills = fields.Integer(string="Number of skills", readonly=True)



    @api.constrains('experience_ids')
    def _check_number_skills(self):
        for record in self:
            record.number_skills = len(record.experience_ids)
            
    @api.model_create_multi
    def create(self, vals_list):

        res = super(ResPartner, self).create(vals_list)
        for record in res:
            if not record.experience_ids:
                    record.experience_ids = [[0, 0, {'skill_id': 2,}]]

            
        record.number_skills = len(record.experience_ids)
        return res
        


class PartnerExperience(models.Model):

    _name = "partner.experience"
    _description = "Contact Experience"

    name = fields.Char(string="Name", compute="_compute_complete_name", store=True, readonly=True)
    skill_id = fields.Many2one("experience", String="skill",required=True)
    years = fields.Integer(string="years",required=True)
    percent = fields.Integer(string="percent", required=True)
    company_id = fields.Many2one('res.company', string='Company',default=lambda self: self.env.company)
    partner_id = fields.Many2one('res.partner', String="Contact")



    @api.depends("skill_id","percent")
    def _compute_complete_name(self):
        for record in self:
            if record.skill_id and record.percent and record.percent > 0:
                record.name = "{0} {1} {2}%".format(record.partner_id.name,record.skill_id.name,record.percent)


class Experience(models.Model):
    _name = "experience"
    _description = "Experience"

    name = fields.Char("Name")
