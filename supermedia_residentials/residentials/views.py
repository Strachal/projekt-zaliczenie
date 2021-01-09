from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Buildings
from .forms import BuildingForm
from .forms import EditBuildingForm
from .filters import BuildingFilter


# funkcja wyświetlająca listę osiedli na stronie głównej
def main(request):
    list_complete = Buildings.objects.all()
    list_all = Buildings.objects.all()
    list_filter = BuildingFilter(request.GET, queryset=list_all)
    return render(request, "index.html", {"filter": list_filter, "list_complete": list_complete})

def filter(request):
    list_all = Buildings.objects.all()
    list_filter = BuildingFilter(request.GET, queryset=list_all)
    return render(request, "filters.html", {"filter": list_filter})

# funkcja edytująca dane osiedlowe (docelowo ze wszystkich modeli)
def edit_buliding(request, id):
    edit = Buildings.objects.get(id=id)
    return render(request, 'edit_building.html', {"Buildings":edit})

# funkcja zapisująca dane osiedlowe (docelowo ze wszystkich modeli)
def save_edited_building(request, id):
    save_edited = Buildings.objects.get(id=id)
    form = EditBuildingForm(request.POST, instance=save_edited)
    if form.is_valid():
        form.save()
        messages.success(request, "zmiany zapisano")
        return render(request, 'edit_building.html', {"Buildings":save_edited})
    else:
        return render(request, 'edit_building.html', {"Buildings":save_edited, "form": form})



# funkcja dodawania osiedla
def add_building(request):
    form = BuildingForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)
        form = BuildingForm
    ctx = {
        'form': form
        }
    return render(request, 'add_building.html', ctx)


# funkcja wyświetlająca wszystkie pola związane z osiedlem (docelowo ze wszystkich modeli)
def raport(request):
    list_complete = Buildings.objects.all()
    return render(request, 'raport.html', {"Buildings":list_complete})

# funkcja logowania
def login(request):
    return render(request, 'login.html')

# funkcja wyszukiwania
def search(request):
    return render(request, 'search.html')

# funkcja dodawania MPK (generuje mail na wskazane adresy email)
def add_mpk(request):
    return render(request, 'add_mpk.html')

# funkcja sumująca ilość HP i LU osiedli wyświetlanych na str. głównej   (default wszsytkie osiedla)
def sum_hp(requet):
    return sum(main(quantity_HP))



