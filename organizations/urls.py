# organizations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('units/create/', views.OrganizationalUnitCreateView.as_view(), name='organizational_unit_create'),
    path('units/', views.OrganizationalUnitListView.as_view(), name='organizational_unit_list'),
    path('units/<int:pk>/update/', views.OrganizationalUnitUpdateView.as_view(), name='organizational_unit_update'),
    path('units/<int:pk>/delete/', views.OrganizationalUnitDeleteView.as_view(), name='organizational_unit_delete'),
]
