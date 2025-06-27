from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar/', views.cadastrar_livro, name='cadastrar_livro'),
    path('livros/', views.livros, name='livros'),
    path('editar/<int:id>/', views.editar_livro, name='editar_livro'),
    path('excluir/<int:livro_id>/', views.confirmar_exclusao, name='confirmar_exclusao'),
    path('alternar_lido/<int:livro_id>/', views.alternar_lido, name='alternar_lido'),
]