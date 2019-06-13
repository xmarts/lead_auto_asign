# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from datetime import datetime, date, time
from dateutil.relativedelta import relativedelta
from odoo import exceptions
from openerp.exceptions import UserError, RedirectWarning, ValidationError




class CrmEstados(models.Model):
    _name = 'crm.estado'
     
    name = fields.Char(string="Estado")
    codigo = fields.Char(string="Code")

class CrmLeadAsign(models.Model):
    _name = "crm.lead.asign"

    name = fields.Char(string="Name")
    r_inicial = fields.Integer(string="Rango inicial")
    r_final = fields.Integer(string="Rango final")
    estado = fields.Many2many("crm.estado",string="Estados")
    tipo_cliente = fields.Selection([('cliente','Cliente'),('proveedor','Proveedor')], string="Tipo Cliente")
    company_id = fields.Many2one("res.company", string="Compañia")
    user_id = fields.Many2one("res.users", string="Vendedor")

class lead_ini(models.Model):
    _inherit='crm.lead'

    piezas=fields.Integer(string='Numero de Piezas', index=True)    
    estado=fields.Char(string='Estado', index=True)
    estado_id=fields.Many2one("crm.estado",string='Estado', index=True)
    type_cliente=fields.Char(string='¿Cliente/provedor?', index=True) 


    @api.model
    def create(self,values):
        if values:
            res = super(lead_ini, self).create(values)
            p = int(res.piezas)
            con = self.env["crm.lead.asign"].search([('tipo_cliente', '=', res.type_cliente)])
            est = self.env["crm.estado"].search([('codigo', '=', res['estado'])], limit=1)
            if est:
                res.estado_id = est.id
            for x in con:
                if est in x.estado and p>=x.r_inicial and p<=x.r_final:
                    res.user_id = x.user_id
                    res.team_id = x.user_id.sale_team_id
                    res.company_id = x.company_id
            return res