from django.shortcuts import render
from django.http import HttpResponse
from .models import Buildings
from .forms import BuildingForm

# funkcja wyświetlająca listę osiedli na stronie głównej
def main(request):
    list_complete = Buildings.objects.all()
    return render(request, 'index.html', {"list_complete": list_complete})

def showlist_years(request):
    return render(request, 'index.html')

# def buildings(request):
#     return HttpResponse("Tu będzie wyswietlana lista osiedli")

def details(request):

    list_detail = Buildings.objects.all()

    return render(request, 'building_detail.html', {"list_detail": list_detail})

def raport(request):
    return render(request, 'raport.html')

# def add_building(request):
#     return render(request, 'add_building.html')

def finances(request):
    return HttpResponse("Tu zobaczymy szczegóły finansowe")

def all_date(request):
    return HttpResponse("Tutaj wyświetlone będą daty związane z danym osiedlem")

def login(request):
    return render(request, 'login.html')

def search(request):
    return render(request, 'search.html')

def add_mpk(request):
    return render(request, 'add_mpk.html')

def add_building(request):
    form = BuildingForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = BuildingForm
    ctx = {
        'form': form
        }
    return render(request, 'add_building.html', ctx)

def sum_hp(requet):
    return sum(main(quantity_HP))



