from django.core.paginator import Paginator
from django.shortcuts import render

from cidade.models import Cidade
from noticia.forms import PesquisaNoticiaForm
from noticia.models import Noticia
from filme.models import Filme
from loja.models import Loja
from duvida.models import Duvida
from categoria.models import Categoria
from promocao.models import Promocao


def index(request):
    lista_noticia = Noticia.objects.all().order_by('id')
    lista_filme = Filme.objects.all().order_by('id')
    lista_loja = Loja.objects.all().order_by('id')
    lista_cidade = Cidade.objects.all().order_by('id')
    print(lista_noticia)
    print(lista_filme)
    print(lista_loja)
    return render(request, 'index.html', {'noticias': lista_noticia,'filmes':lista_filme,'lojas':lista_loja,'cidades':lista_cidade})


def atendimento(request):
    lista_duvida = Duvida.objects.all().order_by('id')
    lista_categoria = Categoria.objects.all().order_by('id')
    return render(request, 'atendimento.html',{'duvidas': lista_duvida,'categorias': lista_categoria})


def noticias(request):
    form=PesquisaNoticiaForm(request.GET)
    if form.is_valid():#nao ha regras de validacao para o campo titulo, linha para mudancas futuras
        titulo=form.cleaned_data['titulo']#recupera o titulo buscado do form
        lista_noticia = Noticia.objects.filter(titulo__icontains=titulo).order_by('id')#filtra as noticias do bd pelo titulo buscado
        paginator=Paginator(lista_noticia,4)# numero de elementos por pagina
        pagina=request.GET.get('pagina')#recupera o parametro de requisicao pagina
        page_obj=paginator.get_page(pagina)#recupera um objeto page conforme a pagina requisitada
        lista_cidade = Cidade.objects.all().order_by('id')
        print(lista_noticia)
        return render(request, 'noticias.html', {'noticias': page_obj,'carrossel':lista_noticia,'cidades': lista_cidade,'form':form})
    else:
        raise ValueError('Ocorreu um erro ao tentar recuperar uma noticia')

def usuario(request):
    lista_promocao = Promocao.objects.all().order_by('id').reverse()
    return render(request, 'usuario.html',{'promocoes': lista_promocao})

