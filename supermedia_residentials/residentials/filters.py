import django_filters
from .models import Buildings

class BuildingFilter(django_filters.FilterSet):
    class Meta():
        model = Buildings
        fields = ["year_Launch_services", "developer", "status", "estimated_budget_accept"]



