from django.shortcuts import render
from django.http import HttpResponse
from .models import Buildings


def main(request):
    list_complete = Buildings.objects.all()
    return render(request, 'index.html', {"list_complete": list_complete})

def showlist_years(request):
    return render(request, 'index.html')

def buildings(request):
    return HttpResponse("Tu będzie wyswietlana lista osiedli")

def details(request):

    list_detail = Buildings.objects.filter()

    return render(request, 'building_detail.html', {"list_detail": list_detail})

def raport(request):
    return render(request, 'raport.html')

def add_building(request):
    return HttpResponse("Tutaj będziemy dodawać osiedla")

def finances(request):
    return HttpResponse("Tu zobaczymy szczegóły finansowe")

def all_date(request):
    return HttpResponse("Tutaj wyświetlone będą daty związane z danym osiedlem")


