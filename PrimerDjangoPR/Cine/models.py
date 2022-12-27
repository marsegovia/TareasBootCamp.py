from django.db import models
from django.urls import reverse

class Director(models.Model):
    name = models.CharField(max_length= 64, help_text=(("Ingresa el nombre del Director ")))
    apellido = models.CharField(max_length=64, help_text=(("Ingresa el apellido del Director")))
    
    def get_absolute_url(self):
        return reverse("Director_detail", args={str: self.name + self.apellido})
    
    
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.apellido
    
class Pelicula(models.Model):
    name_movie = models.CharField(max_length=100, help_text=("Ingrese el nombre de la pelicula"))
    Director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    
    
    def __str__(self):
        return self.name_movie
