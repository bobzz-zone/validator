# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "validator"
app_title = "Validator"
app_publisher = "bobzz.zone@gmail.com"
app_description = "validator double request"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "bobzz.zone@gmail.com"
app_license = "MIT"
doc_events = {
	"Sales Order":{
		"before_save": "validatorvalidator.custom.validate_form"
	},
	"Delivery Note":{
		"before_save": "validator.validator.custom.validate_form"
	},
	"Sales Invoice":{
		"before_save": "validator.validator.custom.validate_form"
	},
	"Journal Entry":{
		"before_save": "validator.validator.custom.validate_form"
	},
	"Purchase Invoice":{
		"before_save": "validator.validator.custom.validate_form"
	},
	"Payment Entry":{
		"before_save": "validator.validator.custom.validate_form"
	},
	"Purchase Order":{
		"before_save": "validator.validator.custom.validate_form"
	},
	"Purchase Receipt":{
		"before_save": "validator.validator.custom.validate_form"
	},
	"Stock Entry":{
		"before_save": "validator.validator.custom.validate_form"
	},
	"Production Order":{
		"before_save": "validator.validator.custom.validate_form"
	},

}
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/validator/css/validator.css"
# app_include_js = "/assets/validator/js/validator.js"

# include js, css files in header of web template
# web_include_css = "/assets/validator/css/validator.css"
# web_include_js = "/assets/validator/js/validator.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "validator.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "validator.install.before_install"
# after_install = "validator.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "validator.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"validator.tasks.all"
# 	],
# 	"daily": [
# 		"validator.tasks.daily"
# 	],
# 	"hourly": [
# 		"validator.tasks.hourly"
# 	],
# 	"weekly": [
# 		"validator.tasks.weekly"
# 	]
# 	"monthly": [
# 		"validator.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "validator.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "validator.event.get_events"
# }

