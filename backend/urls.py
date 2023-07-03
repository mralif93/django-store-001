from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.DashboardView, name="dashboard_view"),
    path('users/', views.UsersView, name="users_view"),
    path('user/add/', views.UserAddView, name="user_add_view"),
    path('user/update/<int:id>/', views.UserUpdateView, name="user_update_view"),
]