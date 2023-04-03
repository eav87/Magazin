from django.shortcuts import render,redirect
from .models import Auto
from .forms import AutoForm
from django.views.generic import DetailView,UpdateView


class NewUpdateView(UpdateView):
    model = Auto
    template_name = 'pervi_sait/forma_auto.html'

    form_class = AutoForm
    # fields = ['marka', 'model', 'harakteristika', 'data']


def glavnaya(request):
    return render(request,'pervi_sait/glavnaya.html')

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
    asd = Auto.objects.all()
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
