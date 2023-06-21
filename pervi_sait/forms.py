from .models import Auto
from django.forms import ModelForm, TextInput, DateInput, Textarea, PasswordInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# create forma zapolnenia avto:
class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['marka','model','harakteristika','data']

        widgets = {   
            "marka": ChoiceField(choices = Auto.objects.distinct('marka'), widget = Select(attrs = {'class' : 'form-control'})),
            "model": ChoiceField(choices = Auto.objects.distinct('model'), widget = Select(attrs = {'class' : 'form-control'})),
            
            'harakteristika' : Textarea(attrs = {
                'class' : 'form-control',
                'placeholder' : 'Характеристика авто'
            }),
            'data' : DateInput(attrs = {
                'class' : 'form-control',
                'placeholder':'Дата публикации авто'
            })
        }

class Vibor_AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['marka','model']
        widgets = {
            'marka':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите марку автомобиля'
        }),
            'model':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите модель автомобиля'
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

