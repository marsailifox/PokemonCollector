from django.db import models
from django.urls import reverse


# Create your models here.
class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('pokemons', kwargs={'pokemon_id': self.id})

class Squad(models.Model):
  name = models.CharField(max_length=100)
  pokemons = models.ManyToManyField(Pokemon)


  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('squads', kwargs={'squad_id': self.id})

squad = models.ForeignKey(
  Squad,
  on_delete=models.CASCADE
)

pokemon = models.ForeignKey(
  Pokemon,
  on_delete=models.CASCADE
)

class Photo(models.Model):
  url = models.CharField(max_length=200)
  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for pokemon_id: {self.pokemon_id} @{self.url}"