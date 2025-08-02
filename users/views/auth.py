from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from users.forms import UserRegisterForm, UserUpdateForm  # você precisa garantir que esses formulários existam

User = get_user_model()

# --- Autenticação ---
class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('feed')  # ajuste conforme sua view inicial

class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'


# --- Registro ---
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


# --- Perfil e Edição ---
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


# --- Troca de senha (usuário autenticado) ---
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'users/password/change_form.html'
    success_url = reverse_lazy('password_change_done')

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'users/password/change_done.html'


# --- Redefinição de senha (via e-mail) ---
class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password/reset_form.html'
    email_template_name = 'users/password/reset_email.html'  # opcional
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password/reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password/reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password/reset_complete.html'
