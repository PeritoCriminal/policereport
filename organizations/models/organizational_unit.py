# policereport/core/models.py
from django.db import models

class OrganizationalUnit(models.Model):
    """
    Representa uma unidade organizacional dentro de uma instituição de segurança pública.
    Pode ser uma Instituição, Divisão, Departamento ou Subdivisão,
    organizada em uma hierarquia.
    """

    # Nome da unidade (ex: "Polícia Civil", "1º Batalhão de PM", "Núcleo de Perícias Criminalísticas de Americana")
    name = models.CharField(
        max_length=255,
        unique=True, # Garante que cada nome de unidade seja único no sistema
        verbose_name="Nome da Unidade"
    )

    # Campo para a abreviação da unidade (ex: PC, PM, SPTC, 1º DP, EPC Limeira)
    abbreviation = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Abreviação"
    )

    # Tipo da unidade para classificá-la na hierarquia (Instituição, Divisão, etc.)
    UNIT_TYPES = (
        ('INSTITUTION', 'Instituição (PC, PM, GCM, etc.)'),
        ('HEADQUARTERS', 'Quartel General / Sede'), # Ex: QG da PM, Sede da SSP
        ('DIVISION', 'Divisão / Comando Geral'), # Ex: Divisão de Homicídios, CPA/M-1
        ('DEPARTMENT', 'Departamento / Batalhão'), # Ex: DEIC, 1º Batalhão de PM
        ('SUBDIVISION', 'Subdivisão / Companhia / Delegacia / Núcleo / Equipe'), # Ex: 1ª Cia, 1º DP, Núcleo de Perícias, Equipe de Perícia
        ('SECTION', 'Seção / Setor'), # Ex: Setor de Cartório, Seção de Armas
        # Adicione mais tipos conforme a necessidade da granularidade
    )
    unit_type = models.CharField(
        max_length=50,
        choices=UNIT_TYPES,
        verbose_name="Tipo de Unidade"
    )

    # Campo para o estado ao qual a unidade pertence (para genericidade em vários estados)
    state = models.CharField(
        max_length=50, # Ex: "SP", "MG", "RJ"
        blank=True,
        null=True,
        verbose_name="Estado"
    )

    # Campo opcional para uma descrição mais detalhada da unidade
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descrição Detalhada"
    )

    # Campo para construir a hierarquia (auto-referência)
    # Uma unidade pode ter uma unidade "pai" (ex: uma Delegacia pertence a uma Seccional)
    parent = models.ForeignKey(
        'self',  # Refere-se à própria classe OrganizationalUnit
        on_delete=models.SET_NULL, # Se a unidade pai for deletada, este campo se torna nulo
        null=True,
        blank=True,
        related_name='children', # Permite acessar as sub-unidades através de parent.children.all()
        verbose_name="Unidade Superior Hierárquica"
    )

    # NOVO CAMPO: Indica se a unidade está ativa ou desativada.
    is_active = models.BooleanField(
        default=True, # Por padrão, novas unidades são ativas
        verbose_name="Ativo"
    )

    class Meta:
        verbose_name = "Unidade Organizacional"
        verbose_name_plural = "Unidades Organizacionais"
        ordering = ['name'] # Ordena por nome por padrão
        # Você pode adicionar unique_together se o nome da unidade precisar ser único apenas
        # dentro de sua unidade pai, e não globalmente (ex: 'Setor A' em dois departamentos diferentes)
        # unique_together = ('name', 'parent')

    def __str__(self):
        """Retorna uma representação legível da unidade, incluindo seu tipo."""
        type_display = self.get_unit_type_display()
        if self.abbreviation:
            return f"{type_display}: {self.name} ({self.abbreviation})"
        return f"{type_display}: {self.name}"

    def get_full_path(self):
        """
        Retorna o caminho hierárquico completo da unidade,
        ex: 'Secretaria de Segurança Pública > Polícia Civil > DEIC > 1ª Delegacia'
        """
        path = [self.name]
        current = self
        while current.parent:
            current = current.parent
            path.insert(0, current.name)
        return " > ".join(path)
    