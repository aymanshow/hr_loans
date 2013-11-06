# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class hr_loan(osv.osv):
    _name = 'hr.loan'
    _description = 'HR Loan'

    _columns = {
        'employee_id': fields.many2one('hr.employee','id','Employee ID'),
	'loan_type': fields.selection((('P','Payment Advance'),
					   ('L','Loan')),'Loan Type'),
        'loan_date': fields.date('Loan Date'),
        'comment': fields.text('Additional Information'),
    }

hr_loan()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
