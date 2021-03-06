from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from models import *


class TolaUserAdmin(admin.ModelAdmin):
	list_filter = ( 'activity_url',)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_date', 'edit_date')
    display = 'Organization'

admin.site.register(TolaUser, TolaUserAdmin)
admin.site.register(Organization, OrganizationAdmin)
