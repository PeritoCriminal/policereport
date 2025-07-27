# organizations/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('', views.HomeView.as_view(), name='home'),
     path('links/', views.LinksView.as_view(), name='links'),
]
