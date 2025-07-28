# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # Importa o UserAdmin padrão
from .models import User # Importa o seu modelo User personalizado

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Classe Admin para o modelo User personalizado.
    Estende BaseUserAdmin para manter a funcionalidade padrão do Django
    e adiciona campos personalizados.
    """
    # Campos a serem exibidos na lista de usuários no admin
    list_display = (
        'username',
        'display_name',
        'email',
        'is_staff',
        'is_active',
        'organizational_unit', # Seu campo personalizado
        'role', # Seu campo personalizado
        'dark_theme', # Seu campo personalizado
    )

    # Campos para filtrar a lista de usuários
    list_filter = (
        'is_staff',
        'is_active',
        'is_superuser',
        'organizational_unit', # Seu campo personalizado
        'role', # Seu campo personalizado
        'grammatical_gender', # Seu campo personalizado
        'dark_theme', # Seu campo personalizado
    )

    # Campos para pesquisa
    search_fields = (
        'username',
        'display_name',
        'email',
        'first_name',
        'last_name',
    )

    # Campos que usarão um widget de seleção bruta (melhor para muitos FKs)
    raw_id_fields = (
        'organizational_unit', # Seu campo personalizado
    )

    # Organização dos campos no formulário de edição/criação de usuário no admin
    # Isso substitui os fieldsets padrão de AbstractUser e adiciona seus campos.
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email', 'display_name', 'grammatical_gender', 'dark_theme')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Detalhes Organizacionais', {'fields': ('organizational_unit', 'role')}), # Novo fieldset para seus campos
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Ordem dos campos no formulário de adição de novo usuário (add_fieldsets)
    # Isso é importante para o formulário de criação de usuário no admin.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'password2'), # password2 é para confirmação de senha
        }),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email', 'display_name', 'grammatical_gender', 'dark_theme')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Detalhes Organizacionais', {'fields': ('organizational_unit', 'role')}),
    )
