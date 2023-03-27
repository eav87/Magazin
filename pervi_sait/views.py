from django.shortcuts import render


def glavnaya(request):
    return render(request,'pervi_sait/glavnaya.html')

def pervaya(request):
    return render(request, 'pervi_sait/pervaya.html')

def vtoraya(request):
    return render (request, 'pervi_sait/vtoraya.html')

def tretya(request):
    return render(request, 'pervi_sait/tretya.html')

def vse_auto(request):
    return render(request, 'pervi_sait/vse_auto.html')


