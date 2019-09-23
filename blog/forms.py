from django import forms

from .models import Publicaciones

class FormPub(forms.ModelForm):

    class Meta:
        model = Publicaciones
        fields = ('titulo', 'texto',)
