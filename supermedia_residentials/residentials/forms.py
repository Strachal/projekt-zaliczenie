from django import forms

from .models import Buildings

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Buildings
        fields = [
            "KI_number",
            "building_name",
            "building_adres",
            "GPON_node_localisation",
            "quantity_HP",
            "quantity_LU",
            "kind_of_inhabitation",
            "status",
            "remarks_of_MS"
        ]