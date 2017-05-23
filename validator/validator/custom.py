from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class custom(Document):
	pass
@frappe.whitelist()
def validate_form(doc,method):
	check = frappe.db.sql("select name,creation from `tab{}` where DATE_FORMAT(creation,'%b %d %Y %H:%i') = DATE_FORMAT('{}','%b %d %Y %H:%i') and owner = '{}' ".format(doc.doctype,doc.creation,frappe.session.user),as_list=1)
	for data in check:
		frappe.throw("Double Request Detected please reload and check {}".format(data[0]))