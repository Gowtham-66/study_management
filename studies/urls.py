
from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('study/<int:pk>/', views.study_detail, name='study_detail'),
    path('study/new/', views.study_create, name='study_create'),
    path('study/<int:pk>/edit/', views.study_update, name='study_update'),
    path('study/<int:pk>/delete/', views.study_delete, name='study_delete'),
]