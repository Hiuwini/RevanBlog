from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
