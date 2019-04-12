frappe.ui.form.on('Employee', {
	onload: function(frm) {
		if(frm.doc.date_of_birth){
			console.log("frm.doc.date_of_birth",frm.doc.date_of_birth);
			let days = frappe.datetime.get_day_diff(frappe.datetime.nowdate(),frm.doc.date_of_birth);
			frm.set_value("age", Math.floor((days).toFixed(2) / 365.25));
			frm.refresh_field("age");
		}
		if(frm.doc.date_of_joining){
			console.log("frm.doc.date_of_joining",frm.doc.date_of_joining);
			let days = frappe.datetime.get_day_diff(frappe.datetime.nowdate(),frm.doc.date_of_joining);
			frm.set_value("years_experience", Math.floor((days).toFixed(2) / 365.25));
			frm.refresh_field("years_experience");

		}
		if(frm.is_dirty()){
			frm.save();
		}
  },
	date_of_joining:function(frm) {
		let days = frappe.datetime.get_day_diff(frappe.datetime.nowdate(),frm.doc.date_of_joining);
		frm.set_value("years_experience", Math.floor((days).toFixed(2) / 365.25));
    frm.refresh_field("years_experience");
},
	date_of_birth: function(frm) {
		let days = frappe.datetime.get_day_diff(frappe.datetime.nowdate(),frm.doc.date_of_birth);
		frm.set_value("age", Math.floor((days).toFixed(2) / 365.25));
    frm.refresh_field("age");

	}
});
