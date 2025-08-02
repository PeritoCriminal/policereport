from django.urls import path
from users.views import (
    CustomLoginView,
    CustomLogoutView,
    CustomPasswordChangeView,
    CustomPasswordChangeDoneView,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    RegisterView,              # <- ADICIONE ESTA
    ProfileView,               # <- E ESTA
    EditProfileView,           # <- E ESTA
)

urlpatterns = [
    # Autenticação
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),  # <- REGISTRO

    # Perfil
    path('profile/', ProfileView.as_view(), name='profile'),                # <- PERFIL
    path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),  # <- EDIÇÃO

    # Troca de senha (usuário autenticado)
    path('password/change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password/change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),

    # Redefinição de senha (via e-mail)
    path('password/reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
