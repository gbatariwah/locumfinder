from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<str:uid>/', views.job_detail, name='job_detail'),

]
