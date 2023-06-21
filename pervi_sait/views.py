from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Auto
from .forms import AutoForm, Vibor_AutoForm, RegisterUserForm
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView

PER_PAGE = 4 # Количество записей на странице

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'pervi_sait/register.html'
    success_url = reverse_lazy('glavnaya')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('glavnaya')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'pervi_sait/login.html'

    def get_success_url(self):
        return reverse_lazy('glavnaya')

def logout_user(request):
    logout(request)
    return redirect('login')

class NewDetailView(DetailView):
    model = Auto
    template_name = 'pervi_sait/details_view.html'
    context_object_name = 'auto'


class NewUpdateView(UpdateView):
    model = Auto
    template_name = 'pervi_sait/forma_auto.html'

    form_class = AutoForm

class NewDeleteView(DeleteView):
    model = Auto
    success_url = '/vse_auto'

    template_name = 'pervi_sait/delete_auto.html'




def glavnaya(request):
        form1 = Vibor_AutoForm(request.GET)
        return render(request,'pervi_sait/glavnaya.html',{'form1':form1, 'marks':marks, 'models':models})


def show_auto_mersedes(request):
    return show_auto(request, marka='Mersedes')

def show_auto_bmw(request):
    return show_auto(request, marka='BMW')

def show_auto_audi(request):
    return show_auto(request, marka='Audi')

def show_auto(request, marka: str):
    models = Auto.objects.filter(marka = marka)
    paginator = Paginator(models, PER_PAGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pervi_sait/show_auto.html',{'page_obj':page_obj, 'marka':marka})


def zapis_to(request):
    form = Auto.objects.all()
    return render(request,'pervi_sait/zapis_na_to.html',{'form':form})



def akcii(request):
    return render(request,'pervi_sait/Akcii.html')

def vse_auto(request):
    asd = Auto.objects.all().order_by('-data')
    paginator = Paginator(asd,4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pervi_sait/vse_auto.html',{'page_obj': page_obj})



def forma_auto(request):
    error = ''
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('glavnaya')
        else:
            error = 'Форма не верна'

    form = AutoForm

    data = {
        'form' : form,
        'error': error
    }
    return render(request, 'pervi_sait/forma_auto.html',data)

def vibor_auto_glavnaya(request):
    error = ''
    if request.method == 'GET':
        form1=AutoForm(request.GET)
        if form1.is_valid():
            return {{form1}}
        else:
            error = 'Форма не верна'

    form1 = Vibor_AutoForm

    data1 = {
        'form1' : form1,
        'error': error
    }
    return render(request, 'pervi_sait/vibran_auto.html', data1)


