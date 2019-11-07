# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, RedirectWarning, ValidationError

class ticket(models.Model):
	_name = 'crm.lead'
	_inherit = 'crm.lead'

	employee_id  = fields.Many2one("res.users" ,string="Employee")
	packages_ids = fields.One2many('packages.voyage_packages','ticket_id', string="Voyages")
	
	ticket_source = fields.Selection(selection=[('key_1','whatsApp') , ('key_2','phone') , ('key_3','email')] )
	typee        = fields.Char()
	
	cost         = fields.Float(readonly=True)
	selling      = fields.Float(readonly=True)
	commission    = fields.Float(readonly=True)
	planned_revenue = fields.Monetary(compute ="_compute_revenue",readonly = True ,store=True)

	number_of_packs       = fields.Selection(selection=[(x+1,x+1) for x in range(15)])
	number_of_destinations = fields.Selection(selection=[(x+1,x+1) for x in range(5)]) 

	@api.onchange("cost","commission")
	def _compute_revenue(self):
		for rec in self:
			rec.planned_revenue = rec.cost * (rec.commission/100.0)


	# @api.depends("planned_revenue_compute")
	# def _assign_planned_revenu(self):
	# 	for rec in self:
	# 		rec.planned_revenue = rec.planned_revenue_compute
	# @api.onchange(packages)


	def compute_total_cost(self):
		self.cost = 0
		self.selling = 0
		for rec in self.packages_ids:
			self.cost    += rec.cost
			self.selling += rec.cost * (1+rec.commission/100.0)
		self.commission      = 0 if (self.cost == 0) else self.selling/self.cost - 1
		self.commission    *=100
		self.planned_revenue = self.cost * (self.commission/100.0)


class packages_voy(models.Model):

	_name = 'packages.voyage_packages'
	
	_description = """"
		This is a description of the module
	"""

	name        = fields.Char()
	packge_type = fields.Selection(selection=[('Hotel','Hotel') , 
											  ('Flight','Flight') , 
											  ('Tour','Tour'),
											  ('Transportation','Transportation'),
											  ('Restraunts','Restraunts')
											  ])
	cost        = fields.Integer()
	commission   = fields.Integer()
	ticket_id  = fields.Many2one("crm.lead")
	checkin_date  = fields.Date()
	checkout_date = fields.Date()
	stars =  fields.Selection(selection = [(1,'1'),(2,'2'),(3,'3')
							   ,(4,'4'),(5,'5')])

