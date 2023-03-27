from django.urls import path
from . import views
urlpatterns = [
    path('',views.glavnaya,name = 'glavnaya'),
    path('pervaya', views.pervaya, name='pervaya'),
    path('vtoraya', views.vtoraya, name='vtoraya'),
    path('tretya', views.tretya, name='tretya'),
    path('vse_auto', views.vse_auto, name='vse_auto')
]