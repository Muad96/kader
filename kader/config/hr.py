from __future__ import unicode_literals
from frappe import _


def get_data():
    return [{
        "label":
        _("Recruitment"),
        "items": [{
            "type": "doctype",
            "name": "Job Contract",
            "description": _("Job Contract"),
        }, {
            "type": "doctype",
            "name": "Contract Renewal",
            "description": _("Contract Renewal"),
        }]
    }, {
        "label":
        _("Employee Lifecycle"),
        "items": [{
            "type": "doctype",
            "name": "Vacation Settlement",
            "description": _("Vacation Settlement"),
        }, {
            "type": "doctype",
            "name": "Joining Work",
            "description": _("Joining Work"),
        }, {
            "type": "doctype",
            "name": "Final Settlement",
            "description": _("Final Settlement"),
        }]
    }, {
        "label":
        _("Travel and Expense Claim"),
        "items": [{
            "type": "doctype",
            "name": "Mandate Form",
            "description": _("Mandate Form"),
        }, {
            "type": "doctype",
            "name": "Business Trip Fees",
            "description": _("Business Trip Fees"),
        }]
    }, {
        "label":
        _("Payroll"),
        "items": [{
            "type": "doctype",
            "name": "Increment Request",
            "description": _("Increment Request"),
        }, {
            "type": "doctype",
            "name": "Modification Salary",
            "label": _("Modification Salary"),
            "description": _(" ")
        }, {
            "type": "doctype",
            "name": "Rewards",
            "label": _("Rewards"),
            "description": _(" ")
        }, {
            "type": "doctype",
            "name": "Deduction",
            "description": _("Deduction"),
        }]
    }, {
        "label":
        _("Employee Document"),
        "items": [{
            "type": "doctype",
            "name": "Issuance Documents",
            "description": _("Issuance Documents"),
        }, {
            "type": "doctype",
            "name": "Employee Clearance",
            "description": _("Employee Clearance"),
        }, {
            "type": "doctype",
            "name": "Visa Request",
            "description": _("Visa Request"),
        }]
    }, {
        "label":
        _("Fleet Management"),
        "items": [{
            "type": "doctype",
            "name": "Vehicle Repairing Request",
            "description": _("Vehicle Repairing Request"),
        }, {
            "type": "doctype",
            "name": "Automobile GP",
            "description": _("Automobile GP"),
        }, {
            "type": "doctype",
            "name": "Receiving Vehicle",
            "description": _("Receiving Vehicle"),
        }]
    }, {
        "label":
        _("Violation"),
        "items": [{
            "type": "doctype",
            "name": "Violation",
            "description": _("Violation"),
        }, {
            "type": "doctype",
            "name": "Violation Type",
            "description": _("Violation Type"),
        }]
    }, {
        "label":
        _("Employee and Attendance"),
        "items": [{
            "type": "doctype",
            "name": "Receipt Custody",
            "description": _("Receipt Custody"),
        }, {
            "type": "doctype",
            "name": "ID Card",
            "description": _("ID Card"),
        }, {
            "type": "doctype",
            "name": "Employee Certificate",
            "description": _("Employee Certificate"),
        }, {
            "type": "doctype",
            "name": "Experience Certificate",
            "description": _("Experience Certificate"),
        }]
    }, {
        "label":
        _("Insurance"),
        "items": [{
            "type": "doctype",
            "name": "Employee Health Insurance",
            "description": _("Employee Health Insurance"),
        }, {
            "type": "doctype",
            "name": "Vehicle Insurance",
            "description": _("Vehicle Insurance Provider"),
        }, {
            "type": "report",
            "label": _("Employee Insurance Table"),
            "name": "Employee Insurance",
            "doctype": "Employee"
        }, {
            "type": "report",
            "label": _("Vehicle Insurance Table"),
            "name": "Vehicle Insurance",
            "doctype": "Vehicle"
        }, {
            "type": "doctype",
            "name": "Property and Facility",
            "description": _("Property and Facility"),
        }, {
            "type": "doctype",
            "name": "Property Insurance Criteria",
            "description": _("Property Insurance Criteria"),
        }]
    }, {
        "label":
        _("Custodies and Telecom"),
        "items": [{
            "type": "doctype",
            "name": "Custody",
            "description": _("Custody"),
        }, {
            "type": "doctype",
            "name": "Custody Log",
            "description": _("Custody Log"),
        }, {
            "type": "doctype",
            "label": _("SIM Cards & Connections"),
            "name": "Telecom",
            "description": _("SIM Cards & Connections"),
        }, {
            "type": "doctype",
            "name": "Custody Type",
            "description": _("Custody Type"),
        }, {
            "type": "doctype",
            "name": "Common Item",
            "description": _("Common Item"),
        }, {
            "type": "doctype",
            "name": "Software Licenses",
            "description": _("Software Licenses"),
        }]
    }]
