from django.db import models
from ckeditor.fields import RichTextField

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='tratamientos/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class SobreMi(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = RichTextField()

    def __str__(self):
        return self.titulo