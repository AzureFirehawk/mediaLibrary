from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.media_list, name='media_list'),
    path('media/<int:pk>/', views.media_detail, name='media_detail'),
    path('add/', views.media_create, name='media_create'),
    path('media/<int:pk>/edit/', views.media_edit, name='media_edit'),
    path('media/<int:pk>/advance_status/', views.media_advance_status, name='media_advance_status'),
]
