# organizations/views/__init__.py (ou organizations/views.py)
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from ..models import OrganizationalUnit
from ..forms import OrganizationalUnitForm

# Exemplo de uma view para criar uma nova unidade organizacional
class OrganizationalUnitCreateView(CreateView):
    model = OrganizationalUnit
    form_class = OrganizationalUnitForm
    template_name = 'organizations/organizational_unit_form.html'
    success_url = reverse_lazy('organizational_unit_list') # Redireciona para uma lista após o sucesso

# Exemplo de uma view para listar unidades organizacionais
class OrganizationalUnitListView(ListView):
    model = OrganizationalUnit
    template_name = 'organizations/organizational_unit_list.html'
    context_object_name = 'organizational_units'
    paginate_by = 10 # Opcional: paginação

# Exemplo de uma view para atualizar uma unidade organizacional
class OrganizationalUnitUpdateView(UpdateView):
    model = OrganizationalUnit
    form_class = OrganizationalUnitForm
    template_name = 'organizations/organizational_unit_form.html'
    success_url = reverse_lazy('organizational_unit_list')

# Exemplo de uma view para deletar uma unidade organizacional
class OrganizationalUnitDeleteView(DeleteView):
    model = OrganizationalUnit
    template_name = 'organizations/organizational_unit_confirm_delete.html'
    success_url = reverse_lazy('organizational_unit_list')