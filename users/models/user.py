# users/models/user.py
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from organizations.models import OrganizationalUnit

class User(AbstractUser):
    """
    Representa um usuário do sistema, estendendo o modelo de usuário padrão do Django
    para incluir informações básicas de perfil, vínculo a uma unidade organizacional,
    função e preferências de interface.

    Este modelo é integrado ao sistema de autenticação do Django e pode ser
    estendido futuramente para incluir mais detalhes ou comportamentos.
    """

    # O campo 'id' (UUIDField) já é definido aqui e irá sobrescrever o PK padrão de AbstractUser (int).
    # Isso é importante para manter o UUID como chave primária.
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID do Usuário"
    )

    # O campo 'username' já vem de AbstractUser. Você pode mantê-lo ou
    # remover e definir um campo diferente como USERNAME_FIELD em settings.py
    # (ex: email). Se mantiver, ele será usado para login.

    display_name = models.CharField(
        max_length=255,
        verbose_name="Nome de Exibição",
        blank=True, # Adicionado blank=True para ser opcional se não for o username
        null=True,
    )

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    grammatical_gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        verbose_name="Gênero Gramatical"
    )

    organizational_unit = models.ForeignKey(
        OrganizationalUnit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        verbose_name="Unidade Organizacional"
    )

    ROLE_CHOICES = (
        ('ADMIN', 'Administrador'),
        ('ANALYST', 'Analista'),
        ('OFFICER', 'Oficial'),
        ('AGENT', 'Agente'),
        ('OTHER', 'Outro'),
    )
    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        verbose_name="Função",
        default='OTHER',
    )

    dark_theme = models.BooleanField(
        default=False,
        verbose_name="Tema Escuro Ativado"
    )

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ['display_name']

    def __str__(self):
        return self.display_name or self.username
