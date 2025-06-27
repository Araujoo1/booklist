from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm

def home(request):
    return render(request, 'home.html')

def cadastrar_livro(request):
    livros = Livro.objects.all()
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livros')
    else:
        form = LivroForm
    
    return render(request, 'cadastrar_livro.html', {'form': form} )

def livros(request): 
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})

