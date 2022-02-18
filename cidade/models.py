from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=70,db_index=True,unique=True)
    slug = models.SlugField(max_length=70)

    class Meta:
        db_table='cidade'

    def __str__(self):
        return self.nome