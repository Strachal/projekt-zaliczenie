from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse("Strona Główna")

def buildings(request):
    return HttpResponse("Tu będzie wyswietlana lista osiedli")

def details(request):
    return HttpResponse("Szczegóły osiedla")

def raport(request):
    return HttpResponse("Raport")

def add_building(request):
    return HttpResponse("Tutaj będziemy dodawać osiedla")

def finances(request):
    return HttpResponse("Tu zobaczymy szczegóły finansowe")

def all_date(request):
    return HttpResponse("Tutaj wyświetlone będą daty związane z danym osiedlem")


