from django.urls import path, include
from .views import PokemonView


#API endpoints
urlpatterns = [
    path('unownedpokemon/',PokemonView.GetUnknownPokemon.as_view()),
    path('mypokemon/',PokemonView.GetMyPokemon.as_view()),
    path('allpokemon/',PokemonView.GetAllPokemon.as_view()),
    path('addpokemon/',PokemonView.AddPokemon.as_view()),
    path('releasepokemon/',PokemonView.RemovePokemon.as_view()),
]