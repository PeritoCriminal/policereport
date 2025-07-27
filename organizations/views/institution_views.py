# organizations/views/institution_views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from organizations.models import Institution # Importa o modelo Institution
from organizations.forms.institution import InstitutionForm # Importa o formulário InstitutionForm

class InstitutionCreateView(CreateView):
    """
    View para criar uma nova Instituição.
    Utiliza InstitutionForm para a validação e renderiza 'institution_form.html'.
    Redireciona para a lista de instituições após o sucesso.
    """
    model = Institution
    form_class = InstitutionForm
    template_name = 'organizations/institution_form.html'
    success_url = reverse_lazy('institution_list')

class InstitutionListView(ListView):
    """
    View para listar todas as Instituições.
    Renderiza 'institution_list.html' e passa a lista de instituições para o template.
    """
    model = Institution
    template_name = 'organizations/institution_list.html'
    context_object_name = 'institutions' # Nome da variável no template para a lista de objetos
    paginate_by = 10 # Opcional: para paginar os resultados

class InstitutionUpdateView(UpdateView):
    """
    View para atualizar uma Instituição existente.
    Utiliza InstitutionForm para a validação e renderiza 'institution_form.html'.
    Redireciona para a lista de instituições após o sucesso.
    """
    model = Institution
    form_class = InstitutionForm
    template_name = 'organizations/institution_form.html'
    success_url = reverse_lazy('institution_list')

class InstitutionDeleteView(DeleteView):
    """
    View para deletar uma Instituição.
    Renderiza 'institution_confirm_delete.html' para confirmação.
    Redireciona para a lista de instituições após a exclusão.
    """
    model = Institution
    template_name = 'organizations/institution_confirm_delete.html'
    success_url = reverse_lazy('institution_list')

