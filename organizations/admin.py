# policereport/organizations/admin.py

from django.contrib import admin
from .models import OrganizationalUnit, Institution # Importa também o modelo Institution

@admin.register(OrganizationalUnit)
class OrganizationalUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'parent', 'abbreviation', 'is_active') 
    list_filter = ('institution', 'is_active') 
    search_fields = ('name', 'abbreviation', 'description')
    raw_id_fields = ('parent', 'institution')

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym', 'state')
    list_filter = ('state',)
    search_fields = ('name', 'acronym', 'description')