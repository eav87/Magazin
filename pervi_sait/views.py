from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Auto
from .forms import AutoForm, Vibor_AutoForm, RegisterUserForm
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView


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
        form1 = Vibor_AutoForm(request.POST)
        return render(request,'pervi_sait/glavnaya.html',{'form1':form1})


def pervaya(request):
    asd = Auto.objects.filter(marka = 'MERSEDES-BENZ')
    paginator = Paginator(asd, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pervi_sait/pervaya.html',{'page_obj':page_obj})


def vtoraya(request):
    asd = Auto.objects.filter(marka = 'BMW')
    paginator = Paginator(asd, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render (request, 'pervi_sait/vtoraya.html',{'page_obj':page_obj})


def tretya(request):
    asd = Auto.objects.filter(marka = 'AUDI')
    paginator = Paginator(asd, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pervi_sait/tretya.html',{'page_obj':page_obj})


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
    if request.method == 'POST':
        form1=AutoForm(request.POST)
        if form1.is_valid():
            return
            # return redirect('vse_auto')
        else:
            error = 'Форма не верна'

    form1 = Vibor_AutoForm

    data1 = {
        'form1' : form1,
        'error': error
    }
    return render(request, 'pervi_sait/vibran_auto.html', data1)


