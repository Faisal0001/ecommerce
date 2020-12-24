from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
	list_display = ('email', 'username', 'date_joined', 'last_login', 'is_active', 'is_superuser','is_admin', 'is_staff')
	search_fields =  ('email', 'username', 'date_joined', 'last_login', 'is_superuser', 'is_active', 'is_admin', 'is_staff')
	readonly_fields = ('date_joined', 'last_login',)
	filter_horizontal = ()
	list_filter = ()
	ordering = ('email',)
	fieldsets = ()

admin.site.register(User, UserAdmin)
