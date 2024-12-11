from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doadores/', views.doador_list, name='doador_list'),
    path('doadores/novo/', views.doador_create, name='doador_create'),
    path('doadores/<int:pk>/', views.doador_detail, name='doador_detail'),
    path('doadores/<int:pk>/editar/', views.doador_update, name='doador_update'),
    path('doadores/<int:pk>/excluir/', views.doador_delete, name='doador_delete'),
    path('doacoes/', views.doacao_list, name='doacao_list'),
    path('doacoes/novo/', views.doacao_create, name='doacao_create'),
    path('doacoes/<int:pk>/', views.doacao_detail, name='doacao_detail'),
    path('doacoes/<int:pk>/editar/', views.doacao_update, name='doacao_update'),
    path('doacoes/<int:pk>/excluir/', views.doacao_delete, name='doacao_delete'),
]
