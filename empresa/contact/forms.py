from tkinter.ttk import LabelFrame
from django import forms

#Formulario
#los attrs, son los atributos, en este caso son las "clases" que le dan el formato en css
class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control', 
            'placeholder':'Nombre',
        }
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Correo Electronico',
        }
    ))
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Deje su comentario',
        }
    ))