from django.contrib import admin
from .models import Competitors, Activities, Developer, General, GPON_node_list

admin.site.register(Competitors)
admin.site.register(Activities)
admin.site.register(General)
admin.site.register(Developer)
admin.site.register(GPON_node_list)



