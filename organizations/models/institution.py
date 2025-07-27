# organizations/models/institution.py
import uuid
from django.db import models

class Institution(models.Model):
    """
    Representa uma instituição de segurança pública ou entidade governamental
    relevante no contexto do sistema. Este modelo visa armazenar informações
    básicas sobre as instituições, permitindo um relacionamento claro com outras
    entidades do sistema, como unidades organizacionais e usuários.

    Futuras melhorias podem incluir a adição de atributos de contato, como
    endereços de e-mail, números de telefone, endereços físicos, URLs de sites,
    e campos para informações regulatórias ou históricas.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID da Instituição"
    )

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Nome da Instituição"
    )

    state = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Unidade Federativa"
    )

    acronym = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Sigla"
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição Detalhada"
    )

    # Imagem do escudo da unidade federativa
    # As imagens serão armazenadas no diretório MEDIA_ROOT/institutions_shields/federative_units/
    federative_unit_shield = models.ImageField(
        upload_to='institutions_shields/federative_units/',
        blank=True,
        null=True,
        verbose_name="Escudo da Unidade Federativa"
    )

    # Imagem do escudo da instituição
    # As imagens serão armazenadas no diretório MEDIA_ROOT/institutions_shields/institutions/
    institution_shield = models.ImageField(
        upload_to='institutions_shields/institutions/',
        blank=True,
        null=True,
        verbose_name="Escudo da Instituição"
    )

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"
        ordering = ['name']

    def __str__(self):
        return self.name
