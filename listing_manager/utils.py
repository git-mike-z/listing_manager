#
from __future__ import unicode_literals
import frappe, erpnext
from frappe import _
import json
from frappe.utils import flt, cstr, nowdate, nowtime
from six import string_types

class InvalidWarehouseCompany(frappe.ValidationError): pass

@frappe.whitelist()
def get_item_code(code=None):
	if code:
		item_code = frappe.db.get_value("Item Barcode", {"barcode": code}, fieldname=["parent"])
		if not item_code:
			item_code = frappe.db.get_value("Item Supplier", {"supplier_part_no": code}, fieldname=["parent"])
			if not item_code:
			item_code = "Not Found!"
	return item_code

@frappe.whitelist()
def hello():
return "Hello"
