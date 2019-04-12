# -*- coding: utf-8 -*-
# Copyright (c) 2019, KABCO and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class VacationSettlement(Document):

	def validate(self):
		la = frappe.get_all("Leave Allocation", fields=["*"],filters={"employee":self.employee}, order_by="creation desc", limit_page_length=1)

		if(len(la) > 0):
			print ("Leave Allocation ={} ".format(la[0]))
