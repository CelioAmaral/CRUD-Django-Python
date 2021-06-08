from django import forms
from .models import Ferramenta


class FerramentaForm(forms.ModelForm):
    class Meta:
        model = Ferramenta
        fields = ['nome', 'valor', 'quantidade']