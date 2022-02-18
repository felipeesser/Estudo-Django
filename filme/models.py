from django.db import models

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=70,db_index=True,unique=True)
    slug = models.SlugField(max_length=70)
    genero = models.CharField(max_length=200)
    imagem = models.CharField(max_length=70,blank=True)

    class Meta:
        db_table='filme'

    def __str__(self):
        return self.titulo