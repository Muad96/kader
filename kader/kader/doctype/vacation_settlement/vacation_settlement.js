// Copyright (c) 2019, KABCO and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vacation Settlement', {
	setup: function(frm) {
  
	  frm.get_basic_hosing = function(earnings) {
		let bh = 0;
		$.each(earnings, function(index, value) {
		  // console.log("value.salary_component = "+ value.salary_component);
		  if (value.component == "Housing" || value.component == "Basic") {
			bh = bh + value.amount;
		  }
		});
		return bh;
	  }
	},
	refresh: function(frm) {
  
	  frm.add_custom_button(__("Calculate Settlement"), function() {
		frm.final_total = 0;
		frm.doc.earnings = [];
		frm.doc.deductions = [];
		frm.total_dedction = 0;
  
		//get last sattlement
		frappe.call({
		  method: 'kader.kader.tools.get_last_settlement',
		  async: false,
		  args: {
			employee: frm.doc.employee,
			doctype: "Vacation Settlement"
		  },
		  callback: function(r) {
			if (r.message) {
			  let diff = frappe.datetime.get_day_diff(frm.doc.posting_date, r.message.posting_date);
			  3
			  console.log("diff", diff);
			  if (diff < 330) {
				frappe.throw(__("Vacation Settlement is not applicable"));
			  }
			}
		  }
		});
  
		//get salary
		frappe.call({
		  "method": "kader.kader.tools.get_salary",
		  async: false,
		  args: {
			employee: frm.doc.employee,
			start_date: frm.doc.start_date,
			end_date: frm.doc.end_date
		  },
		  callback: function(data) {
			//earnings
			$.each(data.message.earnings, function(index, value) {
			  let new_row = frm.add_child("earnings");
			  new_row.component = value.salary_component;
			  new_row.amount = value.amount;
			});
  
			//deductions
			$.each(data.message.deductions, function(index, value) {
			  let new_row = frm.add_child("deductions");
			  new_row.component = value.salary_component;
			  new_row.amount = value.amount;
			  frm.total_dedction = frm.total_dedction + value.amount;
			});
			console.log("frm.total_dedction =", frm.total_dedction);
  
			refresh_field("earnings");
			refresh_field("deductions");
		  }
		});
  
		//get Violation Deduction
		frappe.call({
		  "method": "kader.kader.tools.get_employee_deduction",
		  async: false,
		  args: {
			employee: frm.doc.employee,
			start_date: frm.doc.start_date,
			end_date: frm.doc.end_date
		  },
		  callback: function(data) {
			$.each(data.message, function(index, value) {
			  console.log("data.message", data.message);
			  console.log("value = ", value);
			  let new_row = frm.add_child("deductions");
			  new_row.component = "Violation Deduction";
			  new_row.amount = value.amount;
			  frm.total_dedction = frm.total_dedction + value.amount;
			});
  
			frm.refresh_field("deductions");
			console.log("frm.total_dedction + violation =", frm.total_dedction);
		  }
		});
  
		debugger;
		console.log("frm.doc.last_day_working = " + frm.doc.last_day_working + " frm.doc.date_joining_work = ", frm.doc.date_joining_work);
		let diff = frappe.datetime.get_day_diff(frm.doc.last_day_working, frm.doc.date_joining_work);
		console.log("diff = " + diff);
		let bh = frm.get_basic_hosing(frm.doc.earnings);
		let deserve_yearly = bh / 30 * frm.doc.annual_vacation;
		let deserve_daily = deserve_yearly / 365;
  
		frm.final_total = parseInt(deserve_daily * diff);
  
		frm.set_value("total_benefits", parseInt(frm.final_total) + parseInt(frm.doc.ticket) - parseInt(frm.total_dedction));
		refresh_field("total_benefits");
  
		///////////////////////////////////////////////////////////////////////
	  });
	},
	posting_date: function(frm) {
	  if (frm.doc.posting_date) {
		frappe.call({
		  method: 'erpnext.hr.doctype.payroll_entry.payroll_entry.get_start_end_dates',
		  args: {
			payroll_frequency: "Monthly",
			start_date: frm.doc.posting_date
		  },
		  callback: function(r) {
			if (r.message) {
			  frm.set_value('start_date', r.message.start_date);
			  frm.set_value('end_date', r.message.end_date);
			}
		  }
		});
	  }
	},
	employee: function(frm) {
	  if (frm.doc.employee) {
		//get Leave Application
		frappe.call({
		  method: "frappe.client.get_list",
		  async: false,
		  args: {
			doctype: "Leave Application",
			fields: ["name", "from_date"],
			filters: {
			  "employee": frm.doc.employee,
			  "docstatus": "1"
			},
			order_by: "posting_date desc",
			limit_page_length: 1
		  },
		  callback: function(r) {
			console.log("r", r);
			if (r.message) {
			  frm.set_value("leave_application", r.message[0].name);
			  frm.set_value("last_day_working", r.message[0].from_date);
  
			  frm.refresh_field("leave_application");
			  frm.refresh_field("last_day_working");
			}
		  }
		});
  
		//get Leave Without Pay Days
		frappe.call({
		  method: 'kader.kader.tools.get_leave_without_pay',
		  async: false,
		  args: {
			"employee": frm.doc.employee
		  },
		  callback: function(r) {
			if (r.message) {
			  frm.set_value('leave_without_pay_days', r.message);
			  frm.refresh_field("leave_without_pay_days");
			}
		  }
		});
  
		//get last Joining Work
		frappe.call({
		  method: "frappe.client.get_list",
		  async: false,
		  args: {
			doctype: "Joining Work",
			fields: ["name", "date_of_work_start"],
			filters: {
			  "employee": frm.doc.employee,
			  "docstatus": "1"
			},
			limit_page_length: 1
		  },
		  callback: function(r) {
			console.log("Joining Work = ", r);
			if (r.message) {
			  frm.set_value("last_joining_work", r.message[0].name);
			  frm.set_value("date_joining_work", r.message[0].date_of_work_start);
			  frm.refresh_field("last_joining_work");
			  frm.refresh_field("date_joining_work");
			}
		  }
		});
  
		//get last last_salaryslip
		frappe.call({
		  method: "frappe.client.get_list",
		  async: false,
		  args: {
			doctype: "Salary Slip",
			fields: ["name", "posting_date"],
			filters: {
			  "employee": frm.doc.employee,
			  "docstatus": "1"
			},
			order_by: "posting_date desc",
			limit_page_length: 1
		  },
		  callback: function(r) {
			if (r.message) {
			  frm.set_value("last_salary_slip", r.message[0].name);
			  frm.set_value("salary_slip_posting_date", r.message[0].posting_date);
			  frm.refresh_field("last_salary_slip");
			  frm.refresh_field("salary_slip_posting_date");
			}
		  }
		});
	  }
	},
	ticket: function(frm) {
	  frm.set_value("total_benefits", parseInt(frm.final_total) + parseInt(frm.doc.ticket) - parseInt(frm.total_dedction));
	  refresh_field("total_benefits");
	}
  });