from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('livros/', views.livros, name='livros'),
]