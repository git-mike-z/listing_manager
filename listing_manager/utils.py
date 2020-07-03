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
	return item_code

@frappe.whitelist()
def get_item_code2(code=None):
	if code:
		item_code = frappe.db.get_value("Item Supplier", {"supplier_part_no": code}, fieldname=["parent"])
		if not item_code:
			frappe.throw(_("No Item with Supplier Part No {0}").format(code))
	return item_code
