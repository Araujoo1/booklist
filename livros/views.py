from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm

def home(request):
    return render(request, 'home.html')

def cadastrar_livro(request):
    return render(request, 'cadastrar_livro.html')

def livros(request): 
    return render(request, 'livros.html')

