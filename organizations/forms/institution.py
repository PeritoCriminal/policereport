# organizations/forms/institution.py
from django import forms
from organizations.models import Institution # Importa o modelo Institution

class InstitutionForm(forms.ModelForm):
    """
    Formulário para o modelo Institution.
    Utiliza ModelForm para gerar campos automaticamente e aplica classes Bootstrap.
    """
    class Meta:
        model = Institution
        fields = '__all__' # Inclui todos os campos do modelo

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo da instituição'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: SP, MG, RJ'}),
            'acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sigla da instituição (Ex: SPTC, PC)'}), # Corrigido para TextInput
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descrição detalhada da instituição'}),
            # Campos para seleção de imagem (ImageField usa ClearableFileInput por padrão, que é bom)
            'federative_unit_shield': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'institution_shield': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': 'Nome da Instituição',
            'state': 'Unidade Federativa',
            'acronym': 'Sigla',
            'description': 'Descrição Detalhada',
            'federative_unit_shield': 'Escudo da Unidade Federativa',
            'institution_shield': 'Escudo da Instituição',
        }

        help_texts = {
            'name': 'Nome completo da instituição (ex: Superintendência da Polícia Técnico-Científica).',
            'state': 'Unidade federativa à qual a instituição pertence (ex: SP, MG).',
            'acronym': 'Abreviação ou sigla da instituição (ex: SPTC, PC, PM).',
            'description': 'Informações adicionais sobre a instituição, sua missão e estrutura.',
            'federative_unit_shield': 'Faça upload da imagem do escudo da unidade federativa (estado).',
            'institution_shield': 'Faça upload da imagem do escudo ou logotipo da instituição.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Você pode adicionar lógica de inicialização extra aqui se necessário.
        # Por exemplo, se quiser adicionar classes CSS a campos que não são facilmente
        # estilizados via 'widgets' no Meta (como RadioSelect, CheckboxSelectMultiple)
        # ou para adicionar atributos genéricos a todos os campos.
