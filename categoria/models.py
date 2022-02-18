from django.db import models

# Create your models here.
class Categoria(models.Model):
    titulo = models.CharField(max_length=70,db_index=True,unique=True)
    slug = models.SlugField(max_length=70)
    corpo = models.CharField(max_length=200,unique=True)
    icone = models.CharField(max_length=70,blank=True)

    class Meta:
        db_table='categoria'

    def __str__(self):
        return self.titulo