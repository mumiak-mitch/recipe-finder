from django.urls import path
from .views import search_recipes, home

urlpatterns = [
    path('', home, name='home'),
    path('search/', search_recipes, name='search_recipes'),
]
