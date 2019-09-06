from django.http import HttpResponse
from django.shortcuts import render
import datetime
from informations import infos
def welcome(request):
    context = {}
    date = str(datetime.date.today())
    visitors = infos['num_of_visitors'] + 1
    infos['num_of_visitors'] = visitors
    houzhui = "th"
    if visitors % 10 == 1:
        houzhui = "st"
    elif visitors % 10 == 2:
        houzhui = "nd"
    context['date'] = date
    context['num_of_visitors'] = visitors
    context['num_houzhui'] = houzhui
    return render(request, 'welcome.html', context)

def introduction(request):
    context = {}
    full_name = "Zhou Yangfan"
    species = "Cat"
    birth = "1998-05-12"
    context['full_name'] = full_name
    context['species'] = species
    context['birth'] = birth
    return render(request, 'brief_introduction.html', context)
