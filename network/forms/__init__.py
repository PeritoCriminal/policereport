# users/models.py
import uuid
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# --- Validador de Domínio de E-mail ---
ALLOWED_EMAIL_DOMAINS = [
    '@policiacientifica.sp.gov.br',
    '@policiacivil.sp.gov.br',
    '@policiafederal.gov.br', # Exemplo: Adicione outros domínios conforme necessário
    '@pm.sp.gov.br',
    '@pc.sp.gov.br',
    '@iml.sp.gov.br',
    '@rodoviaria.sp.gov.br',
]

def validate_police_email_domain(value):
    """
    Valida se o domínio do e-mail pertence a um dos domínios das forças policiais permitidos.
    """
    if not any(value.lower().endswith(domain) for domain in ALLOWED_EMAIL_DOMAINS):
        raise ValidationError(
            _('%(value)s não é um domínio de e-mail permitido. '
              'Utilize um domínio institucional válido das forças policiais de SP.'),
            params={'value': value},
            code='invalid_email_domain'
        )

# --- Modelo de Usuário Customizado ---
class CustomUser(AbstractUser):
    """
    Modelo de Usuário Customizado que herda de AbstractUser.
    Permite login via e-mail e impõe restrições de domínio para e-mails institucionais.
    """
    custom_uuid = models.UUIDField( 
        unique=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="UUID do Usuário",
    )

    username = models.CharField(
        _('nome de usuário'),
        max_length=150,
        unique=False,
        help_text=_('Opcional. 150 caracteres ou menos. Letras, dígitos e @/./+/-/_ apenas.'),
        validators=[AbstractUser.username_validator],
        # error_messages={'unique': _("Um usuário com este nome de usuário já existe.")}, # Remover se unique=False
    )

    email = models.EmailField(
        _('endereço de email'),
        unique=True,
        max_length=255,
        validators=[validate_police_email_domain]
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')

    def __str__(self):
        return self.email