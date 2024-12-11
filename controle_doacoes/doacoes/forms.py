from django import forms
from .models import Doador, Doacao

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = '__all__'

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = '__all__'
