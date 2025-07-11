from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'preco', 'lido']
        labels = {
            'titulo': 'Título',
            'preco': 'Preço'
        }
