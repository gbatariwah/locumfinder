from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('add/', views.JobCreateView.as_view(), name='job_add'),
    path('<str:pk>/', views.job_detail, name='job_detail'),
    path('<str:pk>/comments/add', views.add_comment, name='add_comment'),
    path('<str:pk>/comments/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    path('<str:pk>/update', views.JobUpdateView.as_view(), name='job_update'),
    path('<str:pk>/delete', views.JobDeleteView.as_view(), name='job_delete'),
]
