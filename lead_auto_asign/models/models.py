# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime, date, time
from dateutil.relativedelta import relativedelta
from odoo import exceptions
from openerp.exceptions import UserError, RedirectWarning, ValidationError

class CrmEstados(models.Model):
	_name = "crm.estado"

	name = fields.Char(string="Estado")
	codigo = fields.Char(string="Code")
	# name = fields.Selection([
	# 	('aguascalientes','Aguascalientes'),
	# 	('bajacalifornianorte','Baja California Norte'),
	# 	('bajacaliforniasur','Baja California Sur'),
	# 	('campeche','Campeche'),
	# 	('chiapas','Chiapas'),
	# 	('chihuahua','Chihuahua'),
	# 	('coahuila','Coahuila de Zaragoza'),
	# 	('colima','Colima'),
	# 	('df','Ciudad de México'),
	# 	('durango','Durango'),
	# 	('guanajuato','Guanajuato'),
	# 	('guerrero','Guerrero'),
	# 	('hidalgo','Hidalgo'),
	# 	('jalisvo','Jalisco'),
	# 	('michoacan','Michoacán de Ocampo'),
	# 	('morelos','Morelos'),
	# 	('mexico','México'),
	# 	('nayarit','Nayarit'),
	# 	('nuevoleon','Nuevo León'),
	# 	('oaxaca','Oaxaca'),
	# 	('puebla','Puebla'),
	# 	('queretaro','Querétaro'),
	# 	('quintanaroo','Quintana Roo'),
	# 	('sanluispotosi','San Luis Potosí'),
	# 	('sinaloa','Sinaloa'),
	# 	('sonora','Sonora'),
	# 	('tabasco','Tabasco'),
	# 	('tamaulipas','Tamaulipas'),
	# 	('tlaxcala','Tlaxcala'),
	# 	('veracruz','Veracruz de Ignacio de la Llave'),
	# 	('yucatan','Yucatán'),
	# 	('zacatecas','Zacatecas'),
	# 	], string="Estado")

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
	estado=fields.Integer(string='Estado', index=True)
	type_cliente=fields.Char(string='¿Cliente/provedor?', index=True)

	