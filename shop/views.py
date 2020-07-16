from django.shortcuts import render, get_object_or_404
from .models import Item


def shop(request):
    campers = Item.objects.all()
    return render(request, 'shop/offerte.html', {'campers':campers})

def detail(request, camper_id):
    camper = get_object_or_404(Item, pk=camper_id)
    return render(request, 'shop/detail.html', {'camper':camper})
