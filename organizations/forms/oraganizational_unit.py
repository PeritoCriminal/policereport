# organizations/forms/organizational_unit.py
from django import forms
from organizations.models import OrganizationalUnit

class OrganizationalUnitForm(forms.ModelForm):
    """
    Formulário para o modelo OrganizationalUnit.
    Utiliza ModelForm para gerar campos automaticamente e aplica classes Bootstrap.
    """
    class Meta:
        model = OrganizationalUnit
        # Inclui todos os campos do modelo no formulário.
        # Se você quiser excluir algum campo, use 'exclude = [...]'
        # ou liste os campos explicitamente com 'fields = [...]'
        fields = '__all__'

        # Personaliza os widgets para aplicar classes CSS do Bootstrap.
        # Isso garante que os campos do formulário tenham a aparência do Bootstrap.
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome da Unidade'}),
            'unit_type': forms.Select(attrs={'class': 'form-select'}), # 'form-select' para selects do Bootstrap 5+
            'parent': forms.Select(attrs={'class': 'form-select'}),
            'abbreviation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Abreviação'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado (Ex: SP)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descrição detalhada da unidade'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}), # Checkbox tem uma classe diferente
        }

        # Adiciona labels personalizados para os campos, se desejar
        labels = {
            'name': 'Nome da Unidade',
            'unit_type': 'Tipo de Unidade',
            'parent': 'Unidade Superior Hierárquica',
            'abbreviation': 'Abreviação',
            'state': 'Estado',
            'description': 'Descrição Detalhada',
            'is_active': 'Unidade Ativa',
        }

        # Adiciona mensagens de ajuda personalizadas para os campos, se desejar
        help_texts = {
            'parent': 'Selecione a unidade hierarquicamente superior a esta, se houver.',
            'is_active': 'Desmarque para desativar esta unidade sem excluí-la do sistema.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Opcional: Adicionar classes Bootstrap a campos que não são facilmente
        # estilizados via 'widgets' no Meta (ex: RadioSelect, CheckboxSelectMultiple)
        # Ou para adicionar atributos genéricos a todos os campos.
        # Exemplo:
        # for field_name, field in self.fields.items():
        #     if isinstance(field.widget, forms.TextInput) or \
        #        isinstance(field.widget, forms.Textarea) or \
        #        isinstance(field.widget, forms.Select):
        #         field.widget.attrs.update({'class': 'form-control'})
        #     elif isinstance(field.widget, forms.CheckboxInput):
        #         field.widget.attrs.update({'class': 'form-check-input'})
