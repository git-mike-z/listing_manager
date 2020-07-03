#
from __future__ import unicode_literals
import frappe, erpnext
from frappe import _
import json
from frappe.utils import flt, cstr, nowdate, nowtime

from six import string_types

class InvalidWarehouseCompany(frappe.ValidationError): pass

@frappe.whitelist()
def get_item_code(barcode=None, serial_no=None):
	if barcode:
		item_code = frappe.db.get_value("Item Barcode", {"barcode": barcode}, fieldname=["parent"])
		if not item_code:
			frappe.throw(_("No Item with Barcode {0}").format(barcode))
	elif serial_no:
		item_code = frappe.db.get_value("Serial No", serial_no, "item_code")
		if not item_code:
			frappe.throw(_("No Item with Serial No {0}").format(serial_no))

	return item_code
@frappe.whitelist()
def hello():
return "Hello"
