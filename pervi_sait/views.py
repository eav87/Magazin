from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet


from .forms import AutoForm, RegisterUserForm, ZapisToForm
from .models import Auto, Part, Wheels
from .serializers import WheelsSerializer

PER_PAGE = 4  # Количество записей на странице


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
    success_url =  reverse_lazy('glavnaya')

    template_name = 'pervi_sait/delete_auto.html'


def glavnaya(request):
    asd = Auto.objects.all().order_by('-create_date')
    paginator = Paginator(asd, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pervi_sait/glavnaya.html', {'page_obj': page_obj})


def pervaya(request, ):
    asd = Auto.objects.filter(marka='Mersedes')
    paginator = Paginator(asd, PER_PAGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pervi_sait/pervaya.html', {'page_obj': page_obj})


def vtoraya(request):
    asd = Auto.objects.filter(marka='Bmw')
    paginator = Paginator(asd, PER_PAGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pervi_sait/vtoraya.html', {'page_obj': page_obj})


def tretya(request):
    asd = Auto.objects.filter(marka='Audi')
    paginator = Paginator(asd, PER_PAGE)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pervi_sait/tretya.html', {'page_obj': page_obj})


# def show_auto(request, marka: str):
#     models = Auto.objects.filter(marka = marka)
#     paginator = Paginator(models, PER_PAGE)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'pervi_sait/show_auto.html',{'page_obj':page_obj})

@login_required(login_url='/login')
def zapisnato(request):
    error = ''
    if request.method == 'POST':
        form = ZapisToForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('glavnaya')
        else:
            error = 'Данные не верны!!!'

    form = ZapisToForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'pervi_sait/zapis_na_to.html', data)


#


def akcii(request):
    return render(request, 'pervi_sait/akcii.html')


def vse_auto(request):
    asd = Auto.objects.all().order_by('-create_date')
    paginator = Paginator(asd, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pervi_sait/vse_auto.html', {'page_obj': page_obj})


@login_required
def forma_auto(request):
    error = ''
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            return redirect('glavnaya')
        else:
            error = 'Форма не верна'

    form = AutoForm

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'pervi_sait/forma_auto.html', data)


class Parts(ListView):
    model = Part
    template_name = 'pervi_sait/parts.html'
    context_object_name = 'parts'
    paginate_by = 1



class WheelsViewSet(ModelViewSet):
    queryset = Wheels.objects.all()
    serializer_class = WheelsSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filter_fields = ['name']
    search_fields = ['name','opisanie']
    ordering_fields = ['date']
