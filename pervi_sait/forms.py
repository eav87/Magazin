from .models import Auto
from django.forms import ModelForm, TextInput, DateInput, Textarea

class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['marka','model','harakteristika','data']

        widgets = {
            "marka" : TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Марка авто'
            }),
            "model" : TextInput(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Модель авто'
            }),
            'harakteristika' : Textarea(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Характеристика авто'
            }),
            'data' : DateInput(attrs = {
                'class' : 'form-control',
                'placeholder':'Дата публикации авто'
            })
        }
