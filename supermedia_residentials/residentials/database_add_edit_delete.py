from models import Buildings

building = Buildings.objects.create(building_name="Osiedle Testowe1", building_adres="ul. Testowa")
building.save()