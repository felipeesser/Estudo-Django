from django.db import models

class Promocao(models.Model):
    promocao = models.CharField(max_length=70,db_index=True)
    slug = models.SlugField(max_length=70)
    corpo = models.CharField(max_length=200)

    class Meta:
        db_table='promocao'

    def __str__(self):
        return self.promocao
