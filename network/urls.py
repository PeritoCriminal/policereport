from django.urls import path
from network import views

urlpatterns = [
    path('feed/', views.FeedView.as_view(), name='feed'),
]