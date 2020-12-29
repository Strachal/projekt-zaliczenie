"""supermedia_residentials URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from residentials import views
from residentials.views import add_building


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('buildings', views.buildings),
    path('details', views.details),
    path('raport', views.raport),
    path('add_building', views.add_building),
    path('finances', views.finances),
    path('all_date', views.all_date),
    path('showlist_years', views.showlist_years),
    path('add_building', views.add_building),
    path('login', views.login),
    path('search', views.search),
    path('add_mpk', views.add_mpk),
]
