from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pokemons/', views.pokemons_index, name='index'),
    path('pokemons/<int:pokemon_id>/', views.pokemons_detail, name='detail'),
    path('pokemons/create/', views.PokemonCreate.as_view(), name='pokemons_create'),
    path('pokemons/<int:pk>/update/', views.PokemonUpdate.as_view(), name='pokemons_update'),
    path('pokemons/<int:pk>/delete/', views.PokemonDelete.as_view(), name='pokemons_delete'),
    path('squads/create/', views.SquadCreate.as_view(), name='squads_create'),
    path('squads/', views.squads_index, name='squad_index'),
    path('squads/<int:squad_id>/', views.squads_detail, name='squad_detail'),
    path('squads/<int:pk>/update/', views.SquadUpdate.as_view(), name='squads_update'),
    path('squads/<int:pk>/delete/', views.SquadDelete.as_view(), name='squads_delete'),
    path('squads/<int:squad_id>/assoc_pokemon/<int:pokemon_id>/', views.assoc_pokemon, name='assoc_pokemon'),
    path('squads/<int:squad_id>/disassoc_pokemon/<int:pokemon_id>/', views.disassoc_pokemon, name='disassoc_pokemon'),
]
