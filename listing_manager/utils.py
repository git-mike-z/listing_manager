#
from __future__ import unicode_literals
import frappe, erpnext
from frappe import _
import json
from frappe.utils import flt, cstr, nowdate, nowtime

from six import string_types

class InvalidWarehouseCompany(frappe.ValidationError): pass

@frappe.whitelist()
def get_item_code(scancode=None):
	if scancode:
		#try barcode lookup
		item_code = frappe.db.get_value("Item Barcode", {"scancode": barcode}, fieldname=["parent"])
		if not item_code:
			#try supplier code lookup
			item_code = frappe.db.get_value("Item Supplier", {"scancode": supplier_part_no}, fieldname=["parent"]) 
		if not item_code:
			frappe.throw(_("No Item Found").format(scancode))

	return item_code

@frappe.whitelist()
def hello():
	return "Hello Mike"
