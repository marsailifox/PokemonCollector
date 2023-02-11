from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Squad

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def pokemons_index(request):
  pokemons = Pokemon.objects.all()
  return render(request, 'pokemons/index.html', { 'pokemons': pokemons })

def pokemons_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  return render(request, 'pokemons/detail.html', {
    'pokemon': pokemon
  })

def squads_index(request):
  squads = Squad.objects.all()
  return render(request, 'squads/squad_index.html', { 'squads': squads })

def squads_detail(request, squad_id):
  squad = Squad.objects.get(id=squad_id)
  id_list = squad.pokemons.all().values_list('id')
  pokemons_squad_doesnt_have = Pokemon.objects.exclude(id__in=id_list)
  return render(request, 'squads/squad_detail.html', {
    'squad': squad,
    'pokemons': pokemons_squad_doesnt_have
  })


class PokemonCreate(CreateView):
  model = Pokemon
  fields = ['name', 'type', 'description']
  success_url = '/pokemons'


class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['type', 'description']
  success_url = '/pokemons'

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemons'

class SquadCreate(CreateView):
  model = Squad
  fields = ['name']
  success_url = '/squads'

class SquadUpdate(UpdateView):
  model = Squad
  fields = ['name']
  success_url = '/squads'

class SquadDelete(DeleteView):
  model = Squad
  success_url = '/squads'

def assoc_pokemon(request, squad_id, pokemon_id):
  Squad.objects.get(id=squad_id).pokemons.add(pokemon_id)
  return redirect('squad_detail', squad_id=squad_id)

def disassoc_pokemon(request, squad_id, pokemon_id):
  Squad.objects.get(id=squad_id).pokemons.remove(pokemon_id)
  return redirect('squad_detail', squad_id=squad_id)