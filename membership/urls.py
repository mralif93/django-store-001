from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView, name="login"),
    path('logout/', views.LogoutView, name="logout"),
    path('register/', views.RegisterView, name="register"),
    path('index/', views.IndexView, name="index"),
    path('profile/', views.ProfileView, name="profile"),
    path('change-password/', views.ChangePasswordView, name="change_password"),
    path('forgot-password/', views.ForgotPasswordView, name="forgot_password"),
]