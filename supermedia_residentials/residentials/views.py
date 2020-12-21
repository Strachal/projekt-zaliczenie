from django.shortcuts import render
from django.http import HttpResponse
from .models import Buildings


def main(request):
    list_all_buildings = Buildings.objects.all()
    return render(request, 'index.html', {"list_complete": list_all_buildings})

def buildings(request):
    return HttpResponse("Tu będzie wyswietlana lista osiedli")

def details(request):
    return HttpResponse("Szczegóły osiedla")

def raport(request):
    return render(request, 'raport.html')

def add_building(request):
    return HttpResponse("Tutaj będziemy dodawać osiedla")

def finances(request):
    return HttpResponse("Tu zobaczymy szczegóły finansowe")

def all_date(request):
    return HttpResponse("Tutaj wyświetlone będą daty związane z danym osiedlem")


