from django.urls import path
from . import views

urlpatterns = [
    path('images/', views.files_list, name='files_list'),
    path('images/<int:pk>/', views.image_detail, name='image_detail'),
    path('images/upload', views.upload, name='upload')
]
