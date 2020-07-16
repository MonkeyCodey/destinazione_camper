from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('chi-siamo/', views.about, name='about'),
    path('contatti/', views.contacts, name='contacts'),

]
