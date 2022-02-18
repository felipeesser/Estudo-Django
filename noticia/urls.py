
from django.contrib import admin
from django.urls import path

from noticia import views
app_name='noticia'
urlpatterns = [
    path('cadastro_noticia/',views.cadastro_noticia,name="cadastro_noticia"),
    path('exibe_noticia/<int:id>/',views.exibe_noticia,name='exibe_noticia'),
    path('edita_noticia/<int:id>/', views.edita_noticia, name='edita_noticia'),
path('remove_noticia/', views.remove_noticia, name='remove_noticia')
]
