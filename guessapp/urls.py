from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('random/', views.home, name='home'),
    path('ordered/<id>/', views.insequence, name='insequence'),
    
]