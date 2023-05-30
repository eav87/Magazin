from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Auto
from .forms import AutoForm, Vibor_AutoForm, RegisterUserForm
from django.views.generic import DetailView, UpdateView, ListView, CreateView



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'pervi_sait/register.html'
    success_url = reverse_lazy('glavnaya')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('glavnaya')

    def forma_user(request):
        error = ''
        if request.method == 'POST':
            form2 = RegisterUserForm(request.POST)
            if form2.is_valid():
                form2.save()
                return redirect('glavnaya')
            else:
                error = 'Форма не верна'

        form2 = RegisterUserForm

        data2 = {
            'form': form2,
            'error': error
        }
        return render(request, 'pervi_sait/register.html', data2)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'pervi_sait/login.html'

    def get_success_url(self):
        return reverse_lazy('glavnaya')




class NewUpdateView(UpdateView):
    model = Auto
    template_name = 'pervi_sait/forma_auto.html'

    form_class = AutoForm
    fields = ['marka', 'model', 'harakteristika', 'data']


# class VibranAuto(ListView):
#     model = Auto
#     template_name = 'pervi_sait/vibran_auto.html'
#     context_object_name = 'form1'
#     form_class = Vibor_AutoForm
#     fields = ['marka','model']


def glavnaya(request):
    # if request.method=='POST':
        form1 = Vibor_AutoForm(request.POST)
        return render(request,'pervi_sait/glavnaya.html',{'form1':form1})
    # else:
    #     print('пошел в Попу')
    # return render(request,'pervi_sait/glavnaya.html')

def pervaya(request):
    asd = Auto.objects.filter(marka = 'MERSEDES-BENZ')
    return render(request, 'pervi_sait/pervaya.html',{'asd':asd})


def vtoraya(request):
    asd = Auto.objects.filter(marka = 'BMW')
    return render (request, 'pervi_sait/vtoraya.html',{'asd':asd})


def tretya(request):
    asd = Auto.objects.filter(marka = 'AUDI')
    return render(request, 'pervi_sait/tretya.html',{'asd':asd})


def vse_auto(request):
    asd = Auto.objects.all().order_by('-data')
    return render(request, 'pervi_sait/vse_auto.html',{'asd': asd })


class NewDetailView(DetailView):
    model = Auto
    template_name = 'pervi_sait/details_view.html'
    context_object_name = 'auto'

def forma_auto(request):
    error = ''
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vse_auto')
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
            return form1
            # return redirect('vse_auto')
        else:
            error = 'Форма не верна'

    form1 = Vibor_AutoForm

    data1 = {
        'form1' : form1,
        'error': error
    }
    return render(request, 'pervi_sait/vibran_auto.html', data1)

def logout_user(request):
    logout(request)
    return redirect('login')
