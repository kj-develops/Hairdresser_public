# Author Kjærsti L. Bergli, email: klb022@uit.no
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Code to be able to view and edit info about users on the admin page in the browser
class AccountAdmin(UserAdmin):
	list_display = ('email','username','name', 'role',  'about', 'phone','is_admin')
	search_fields = ('email','username','name')
	readonly_fields= ('id', 'is_superuser')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(User, AccountAdmin)