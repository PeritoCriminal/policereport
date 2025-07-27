# organizations/models/organizational_unit.py
import uuid
from django.db import models
from .institution import Institution # Alterado de 'from . import Institution' para evitar circular import

class OrganizationalUnit(models.Model):
    """
    Representa uma unidade organizacional dentro de uma instituição de segurança pública.
    Pode ser uma Instituição, Divisão, Departamento ou Subdivisão,
    organizada em uma hierarquia. Esta unidade é vinculada a uma Instituição
    específica e possui uma chave primária UUID para identificação única.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID da Unidade Organizacional"
    )

    # Relacionamento com a Instituição à qual esta unidade pertence
    institution = models.ForeignKey(
        Institution,
        on_delete=models.SET_NULL, # Se a instituição for deletada, a unidade fica sem instituição
        null=True,
        blank=True,
        related_name='organizational_units', # Permite acessar as unidades a partir da instituição (instituicao.organizational_units.all())
        verbose_name="Instituição"
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Nome da Unidade"
    )

    abbreviation = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Abreviação"
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição Detalhada"
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="Unidade Superior Hierárquica"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Ativo"
    )

    class Meta:
        verbose_name = "Unidade Organizacional"
        verbose_name_plural = "Unidades Organizacionais"
        ordering = ['name']

    def __str__(self):
        return f'{self.institution} - {self.name}'

    def get_full_path(self):
        path = [self.name]
        current = self
        while current.parent:
            current = current.parent
            path.insert(0, current.name)
        return " > ".join(path)
