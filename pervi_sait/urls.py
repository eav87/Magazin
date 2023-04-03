from django.urls import path
from . import views
urlpatterns = [
    path('',views.glavnaya,name = 'glavnaya'),
    path('forma_auto',views.forma_auto,name = 'forma_auto'),
    path('glavnaya',views.glavnaya,name = 'glavnaya'),
    path('pervaya', views.pervaya, name='pervaya'),
    path('vtoraya', views.vtoraya, name='vtoraya'),
    path('tretya', views.tretya, name='tretya'),
    path('vse_auto', views.vse_auto, name='vse_auto'),
    path('<int:pk>',views.NewDetailView.as_view(),name = 'news_detail'),
    path('<int:pk>/update',views.NewUpdateView.as_view(),name = 'news_update')
]