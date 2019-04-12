# -*- coding: utf-8 -*-
# Copyright (c) 2019, KABCO and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from kader.kader.tools import get_daily_rate
from frappe.utils import get_first_day, getdate, add_months, get_last_day


class Violation(Document):

    def before_insert(self):
        def make_deduction(action):
            daily = get_daily_rate(self.employee,
                                   get_first_day(self.posting_date),
                                   get_last_day(self.posting_date))
            print ("daily = {}".format(daily))
            if action == "One day":
                self.deduction = daily
            elif action == "Tow days":
                self.deduction = daily * 2
            elif action == "Three days":
                self.deduction = daily * 3
            elif action == "Five days":
                self.deduction = daily * 5
            elif action == "10%":
                self.deduction = daily * .10
            elif action == "25%":
                self.deduction = daily * .25
            elif action == "50%":
                self.deduction = daily * .50
            elif action == "75%":
                self.deduction = daily * .75

        violation_list = frappe.get_list(
            "Violation",
            filters={
                "employee":
                self.employee,
                "violation_type":
                self.violation_type,
                "posting_date": [
                    "between",
                    [
                        add_months(self.posting_date,
                                   -6),  # to check last 6 months
                        self.posting_date
                    ]
                ]
            },
            order_by="posting_date")

        count = len(violation_list)
        count = count + 1
        self.frequency_count = count
        if self.frequency_count == 1:
            self.action = frappe.db.get_value('Violation Type',
                                              self.violation_type, "first")
        elif self.frequency_count == 2:
            self.action = frappe.db.get_value('Violation Type',
                                              self.violation_type, "second")
        elif self.frequency_count == 3:
            self.action = frappe.db.get_value('Violation Type',
                                              self.violation_type, "third")
        elif self.frequency_count == 4:
            self.action = frappe.db.get_value('Violation Type',
                                              self.violation_type, "fourth")
        else:
            self.action = frappe.db.get_value('Violation Type',
                                              self.violation_type, "fourth")
        make_deduction(self.action)

    def after_insert(self):
        def create_new_deduction(self):
            doc = frappe.get_doc({
                "doctype": "Deduction",
                "employee": self.employee,
                "employee_name": self.employee_name,
                "posting_date": self.posting_date,
                "type": "Violation Detection",
                "violation_type": self.violation_type,
                "violation":self.name,
                "details": self.note,
                "amount": self.deduction
            })
            doc.insert()
            return doc

        deduc = frappe.get_list(
            "Deduction",
            fields=["name"],
            order_by=self.posting_date,
            filters={
                "docstatus":1,
                "posting_date": [
                    "Between", [
                        get_first_day(self.posting_date),
                        get_last_day(self.posting_date)
                    ]
                ],
                "violation_type":
                self.violation_type,
                "employee":
                self.employee
            })

        if deduc:
            doc = deduc[0]
            print ("doc.name = {}".format(doc.name))
            deduction = frappe.get_doc("Deduction", doc.name)
            deduction.cancel()
            doc = create_new_deduction(self)
        elif self.deduction:
            create_new_deduction(self)

    def validate(self):
        if self.docstatus == 1:
            deductions = frappe.get_list("Deduction",filters={"violation":self.name})[0]
            deduction = frappe.get_doc("Deduction", deductions.name)
            deduction.submit()

    # def on_update(self):
    #     deductions = frappe.get_list("Deduction",filters={"violation":self.name})[0]
    #     deduction = frappe.get_doc("Deduction", deductions.name)
    #     deduction.employee = self.employee
    #     deduction.employee_name = self.employee_name
    #     deduction.posting_date = self.posting_date
    #     deduction.type = "Violation Detection"
    #     deduction.violation_type = self.violation_type
    #     deduction.violation = self.name
    #     deduction.details = self.note
    #     deduction.amount = self.deduction
    #     deduction.save()

    def on_cancel(self):
        deductions = frappe.get_list("Deduction",filters={"violation":self.name})[0]
        deduction = frappe.get_doc("Deduction", deductions.name)
        deduction.cancel()

    def on_trash(self):
        deductions = frappe.get_list("Deduction",filters={"violation":self.name})[0]
        deduction = frappe.get_doc("Deduction", deductions.name)
        deduction.delete()