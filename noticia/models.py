from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=70,db_index=True,unique=True)
    slug = models.SlugField(max_length=70)
    corpo = models.CharField(max_length=200,unique=True)
    imagem = models.CharField(max_length=70,blank=True)

    class Meta:
        db_table='noticia'

    def __str__(self):
        return self.titulo