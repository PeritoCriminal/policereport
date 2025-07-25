# policereport/organizations/admin.py

from django.contrib import admin
from .models import OrganizationalUnit

@admin.register(OrganizationalUnit)
class OrganizationalUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit_type', 'parent', 'abbreviation', 'state')
    list_filter = ('unit_type', 'state', 'parent')
    search_fields = ('name', 'abbreviation', 'description')
    raw_id_fields = ('parent',)