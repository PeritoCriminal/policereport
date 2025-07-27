# organizations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # rotas para institutions
    path('institutions/create/', views.InstitutionCreateView.as_view(), name='institution_create'),
    path('institutions/', views.InstitutionListView.as_view(), name='institution_list'),
    path('institutions/<uuid:pk>/update/', views.InstitutionUpdateView.as_view(), name='institution_update'), # Corrigido para <uuid:pk>
    path('institutions/<uuid:pk>/delete/', views.InstitutionDeleteView.as_view(), name='institution_delete'), # Corrigido para <uuid:pk>

    # rotas para organizational_units
    path('units/create/', views.OrganizationalUnitCreateView.as_view(), name='organizational_unit_create'),
    path('units/', views.OrganizationalUnitListView.as_view(), name='organizational_unit_list'),
    path('units/<uuid:pk>/update/', views.OrganizationalUnitUpdateView.as_view(), name='organizational_unit_update'), # Corrigido para <uuid:pk>
    path('units/<uuid:pk>/delete/', views.OrganizationalUnitDeleteView.as_view(), name='organizational_unit_delete'), # Corrigido para <uuid:pk>
]
