from django import forms

from .models import Buildings

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Buildings
        fields = "__all__"
        #     {
        #     "KI_number": "numer KI",
        #     "building_name": "nazwa osiedla",
        #     "building_adres": "adres osiedla",
        #     "GPON_node_localisation": "węzeł GPON",
        #     "quantity_HP": "ilość HP",
        #     "quantity_LU": "ilość LU",
        #     "kind_of_inhabitation": "status zasiedlenia",
        #     "year_Launch_services": "rok budżetowy",
        #     "status": "status",
        #     "developer": "deweloper",
        #     "remarks_of_MS": "uwagi MS",
        # }
