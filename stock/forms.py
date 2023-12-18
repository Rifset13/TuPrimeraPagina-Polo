from django import forms

class InsumoFormulario(forms.Form): 
    nombre = forms.CharField()
    descripcion = forms.CharField()
    cantidad_en_stock = forms.IntegerField()