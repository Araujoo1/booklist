from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm
from django.db.models import Q
import unicodedata

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

def remove_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def livros(request): 
    status = request.GET.get('status')
    busca = request.GET.get('busca')
    livros = Livro.objects.all()

    if status == 'lido':
        livros = livros.filter(lido=True)
    elif status == 'nao_lido':
        livros = livros.filter(lido=False)

    if busca:
        busca_normalizada = remove_acentos(busca).lower()
        livros = [
            livro for livro in livros
            if busca_normalizada in remove_acentos(livro.titulo).lower()
            or busca_normalizada in remove_acentos(livro.autor).lower()
        ]      
    return render(request, 'livros.html', {'livros': livros})

def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('livros')
    else:
        form=LivroForm(instance=livro)

    return render(request, 'editar_livro.html', {'form': form, 'livro': livro})

def confirmar_exclusao(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if request.method == 'POST':
        livro.delete()
        return redirect('livros')
    
def alternar_lido(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    livro.lido = not livro.lido  # Inverte o valor
    livro.save()
    return redirect('livros')  

    