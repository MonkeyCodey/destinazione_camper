from django.shortcuts import render
from shop.models import Item

def home(request):
    campers = Item.objects.order_by('-data_inserzione')[:4]
    return render(request, 'company/home.html', {'campers':campers})

def about(request):
    return render(request, 'company/chi-siamo.html', {})

def contacts(request):
    return render(request, 'company/contatti.html', {})
    
