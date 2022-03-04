from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('<str:username>/profile/', views.profile, name='profile'),
    path('<str:username>/posts/', views.manage_posts, name='manage_posts'),
    path('<str:username>/profile/update', views.update, name='update'),
]
