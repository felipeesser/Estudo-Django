from django import forms
from django.core.validators import RegexValidator

from noticia.models import Noticia

class PesquisaNoticiaForm(forms.Form):
    titulo= forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control form-control-sm','maxlenght':'100'}),
        required=False
    )
class NoticiaForm(forms.ModelForm):
    class Meta:
        model=Noticia
        fields=('titulo','corpo','imagem')

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['titulo'].error_messages={'required':'Campo obrigatório',
            'unique':'Registro Duplicado'}
        self.fields['titulo'].widget.attrs.update({'class':'form-control form-control-sm'})
        self.fields['corpo'].error_messages = {'required': 'Campo obrigatório',
                                                'unique': 'Registro Duplicado'}
        self.fields['corpo'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['imagem'].error_messages = {'required': 'Campo obrigatório',
                                                'unique': 'Registro Duplicado'}
        self.fields['imagem'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['imagem'].validators=[
            RegexValidator(regex='.+\.(jpg|png|gif|bmp|webp)$', message='Nome inválido.')
        ]
        self.fields['imagem'].required=True