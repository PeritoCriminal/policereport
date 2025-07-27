# organizations/forms/organizational_unit.py
from django import forms
from organizations.models import OrganizationalUnit, Institution # Importa Institution também para o queryset

class OrganizationalUnitForm(forms.ModelForm):
    """
    Formulário para o modelo OrganizationalUnit.
    Utiliza ModelForm para gerar campos automaticamente e aplica classes Bootstrap.
    """
    class Meta:
        model = OrganizationalUnit
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Unidade'}),
            'institution': forms.Select(attrs={'class': 'form-select'}), # Adicionado para a Instituição
            'parent': forms.Select(attrs={'class': 'form-select'}),
            'abbreviation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Abreviação'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado (Ex: SP)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descrição detalhada da unidade'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        labels = {
            'name': 'Nome da Unidade',
            'institution': 'Instituição Vinculada', # Adicionado para a Instituição
            'parent': 'Unidade Superior Hierárquica',
            'abbreviation': 'Abreviação',
            'state': 'Estado',
            'description': 'Descrição Detalhada',
            'is_active': 'Unidade Ativa',
        }

        help_texts = {
            'institution': 'Selecione a instituição à qual esta unidade pertence.', # Adicionado para a Instituição
            'parent': 'Selecione a unidade hierarquicamente superior a esta, se houver.',
            'is_active': 'Desmarque para desativar esta unidade sem excluí-la do sistema.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Opcional: Filtrar o queryset para o campo 'institution' se necessário
        # Ex: self.fields['institution'].queryset = Institution.objects.filter(is_active=True)
        # Para o campo 'parent', o raw_id_fields no admin já ajuda, mas em forms puros,
        # você pode querer otimizar o queryset se houver muitas unidades.
