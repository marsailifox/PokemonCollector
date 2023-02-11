import boto3
import uuid
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Pokemon, Squad, Photo

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

def add_photo(request, pokemon_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, pokemon_id=pokemon_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', pokemon_id=pokemon_id)