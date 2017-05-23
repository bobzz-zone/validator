from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class custom(Document):
	pass
@frappe.whitelist()
def validate_form(doc,method):
	check = frappe.db.sql("select name,creation from `tab{}` where DATE_FORMAT(creation,'%b %d %Y %h:%i') = DATE_FORMAT(NOW(),'%b %d %Y %h:%i') and owner = '{}' ".format(doc.doctype,frappe.session.user),as_list=1)
	for data in check:
		frappe.throw("Double Request Detected please reload and check {}".format(data[0]))