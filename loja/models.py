from django.db import models

# Create your models here.
class Loja(models.Model):
    nome = models.CharField(max_length=70,db_index=True,unique=True)
    slug = models.SlugField(max_length=70)
    imagem = models.CharField(max_length=70,blank=True)

    class Meta:
        db_table='loja'

    def __str__(self):
        return self.nome