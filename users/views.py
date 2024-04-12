import random

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('catalog:product_list')


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        verification_code = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        user.verification_code = verification_code

        user.save()
        current_site = self.request.get_host()
        verification_link = f'http://{current_site}/users/confirm/{verification_code}/'
        message = f'Поздравляем с регистрацией! \nДля верификации перейдите по ссылке \n{verification_link}'
        send_mail(
            subject='Регистрация',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False
        )
        print(message)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('catalog:product_list')


def verification_view(request, token):
    user = User.objects.filter(verification_code=token).first()
    if user:
        user.is_active = True
        user.save()

    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('users:login'))
