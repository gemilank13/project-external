# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Assign(models.Model):
    _name = 'assign.assign'
    
    name = fields.Char('CUST CODE / ID', required=True)
    logo_partner = fields.Binary("LOGO", related="partner_id.image", readonly=True)
    partner_id = fields.Many2one('res.partner','PARTNER', required=True)
    logo_perusahaan = fields.Binary("LOGO", related="perusahaan_id.logo", readonly=True)
    perusahaan_id = fields.Many2one('res.company','MY COMPANY', readonly="1", default=lambda self: self.env['res.company']._company_default_get('project_2'))
    customer = fields.Char('CUST NAME', required=True)
    area_id = fields.Many2one('area.area','AREA')
    product_ids = fields.One2many('product.description', 'assign_id',  string="PRODUCT DESCRIPTION")
    email = fields.Char('EMAIL', required=False)
    no_hp = fields.Char('PHONE NUMBER', required=True)
    alamat = fields.Text('HOME ADDRESS', required=True)
    city = fields.Char('CITY')
    zip_code = fields.Char('ZIP CODE')
    house_owner = fields.Char('HOUSE OWNERSHIP')
    home_number = fields.Char('HOME NUMBER')
    office = fields.Text('OFFICE ADDRESS', required=True)
    office_city = fields.Char('CITY')
    office_zip_code = fields.Char('ZIP CODE')
    office_number = fields.Char('OFFICE NUMBER')
    reff_number = fields.Char('REFF NUMBER')
    BCA = fields.Char('VA BCA')
    MANDIRI = fields.Char('VA MANDIRI')
    PERMATA = fields.Char('VA PERMATA')
    assign_to_id = fields.Many2one('res.users','ASSIGN TO')
    nik = fields.Char('NIK')
    birthday = fields.Date('BIRTHDAY')
    age = fields.Integer('AGE')
    sex = fields.Selection([
        ('Male', 'Male'),
        ('Female', 'Female')
        ], string='SEX')

    @api.multi
    def close(self, vals):
        for rec in self:
            rec.write({'status': 'Close'})

    status = fields.Selection([
        ('Open', 'Open'),
        ('Close', 'Close'),
        ], string='STATUS', store=True, default="Open")

    billhistory_ids = fields.One2many('bill.history', 'assign_id',  string="BILL HISTORY")

class Dpd(models.Model):
    _name = 'dpd.dpd'

    name = fields.Char(string="DPD")
    # assign_id = fields.Many2one('assgn.assign', string="Assign")

class Status(models.Model):
    _name = 'status.status'

    name = fields.Char(string="STS")
    # assign_id = fields.Many2one('assgn.assign', string="Assign")

class Area(models.Model):
    _name = 'area.area'

    name = fields.Char(string="AREA")
    # assign_id = fields.Many2one('assgn.assign', string="Assign")

class ProductDescription(models.Model):
    _name = 'product.description'

    agreement = fields.Char('AGREMENT CODE')
    open_date = fields.Date('OPEN DATE')
    wo_date = fields.Date('WO DATE')
    dpd_id = fields.Many2one('dpd.dpd','DEL')
    last_pay = fields.Date('LPD')
    last_payment_ammount = fields.Float(string="LPA")
    name = fields.Char(string="PRODUCT DESCRIPTION")
    total_tagihan = fields.Float(string="TOTAL TAGIHAN")
    minpay_delq = fields.Float(string="MIN PAYMENT")
    recover = fields.Float(string="RECOVER")
    stay_delq = fields.Float(string="STAY")
    lunas_disc = fields.Float(string="LUNAS DISC")
    angs_ke = fields.Char(string="ANGS KE")
    assign_id = fields.Many2one('assgn.assign', string="Assign")

class BillHistory(models.Model):
    _name = 'bill.history'

    name = fields.Char('DESCRIPTION')
    date = fields.Date('DATE')
    status_id = fields.Many2one('status.status','STATUS')
    # angs_ke = fields.Char(string="ANGS KE")
    assign_id = fields.Many2one('assgn.assign', string="Assign")