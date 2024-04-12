from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, ProfileView, generate_new_password, verification_view

app_name = UsersConfig.name

urlpatterns = [
    path('confirm/<str:token>/', verification_view, name='verification'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password')

]
