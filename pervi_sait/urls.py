from django.urls import path
from .import views
from .views import RegisterUser, LoginUser

urlpatterns = [
    path('',views.glavnaya,name = 'glavnaya'),
    path('forma_auto',views.forma_auto,name = 'forma_auto'),
     # path('glavnaya',views.glavnaya,name = 'glavnaya'),
    path('pervaya', views.pervaya, name='pervaya'),
    path('vtoraya', views.vtoraya, name='vtoraya'),
    path('tretya', views.tretya, name='tretya'),
    path('vse_auto', views.vse_auto, name='vse_auto'),
    path('<int:pk>',views.NewDetailView.as_view(),name = 'details_view'),
    path('<int:pk>/update',views.NewUpdateView.as_view(),name = 'update_auto'),
    path('<int:pk>/delete',views.NewDeleteView.as_view(),name = 'delete_auto'),
    path('vibran_auto',views.vibor_auto_glavnaya,name='vibran_auto'),
    path('login',LoginUser.as_view(),name='login'),
    path('logout',views.logout_user,name='logout'),
    path('register',RegisterUser.as_view(),name='register'),
    path('akcii',views.akcii,name = 'akcii'),
    path('zapis_na_to',views.zapis_na_to,name = 'zapis_na_to')
]
