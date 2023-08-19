from .models import Auto, ZapisTo
from django.forms import ModelForm, TextInput, DateInput, Textarea, PasswordInput,DateTimeInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# create forma zapolnenia avto:
class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['marka','model','harakteristika','price']

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
                'placeholder' : 'Состояние автомобиля:'
                                'Пробег:'
                                'Год выпуска:'
            }),
            'price': TextInput(attrs = {
                'class' : 'form-control',
                'placeholder':'Цена автомобиля'
            })
        }

# Create your forms here.lichni kabinet:

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='логин',widget=forms.TextInput(attrs={'class':'form-input','placeholder':'Имя пользователя'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':'form-input','placeholder':'Пароль'}))
    password2 = forms.CharField(label='Повтор пароля',widget=forms.PasswordInput(attrs={'class':'form-input','placeholder':'Повтор пароля'}))
    class Meta:
        model = User
        fields =  ('username','password1','password2' )
        widgets = {
            "username": forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Имя пользователя'
            }),
            "password1":forms.PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'пароль'
            }),
            'password2':forms.PasswordInput(attrs={
                'class': 'form-input',
                'placeholder': 'пароль'
            })
        }


class ZapisToForm(ModelForm):
    class Meta:
        model = ZapisTo
        fields = ['name','name_auto','nomer_auto','date']

        widgets = {'name':forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'имя'
            }),
                'name_auto':forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'название авто'
            }),
                'nomer_auto':forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'номер авто'
            }),
                'date': forms.DateTimeInput(attrs={
                    'class':'form-control',
                    'type':'datetime-local'
                })
        }