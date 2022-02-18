from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.template.defaultfilters import slugify

from noticia.forms import NoticiaForm
from noticia.models import Noticia


def cadastro_noticia(request):
    if request.POST:#vai cadastrar uma noticia
        noticia_id=request.session.get('noticia_id')#recupera o id da noticia no objeto sessao
        if noticia_id:#alteracao no produto
            noticia=get_object_or_404(Noticia,pk=noticia_id)#recupera a noticia se o id ja existe no banco
            noticia_form=NoticiaForm(request.POST,instance=noticia)
        else:#inclusao produto
            noticia_form=NoticiaForm(request.POST)
        if noticia_form.is_valid():#erros de validacao e conversao
           noticia=noticia_form.save(commit=False)
           noticia.slug=slugify(noticia.titulo)
           noticia.save()
           if noticia_id:
               messages.add_message(request,messages.INFO,'Noticia alterada')
               del request.session['noticia_id']
           else:
               messages.add_message(request,messages.INFO,'noticia cadastrada com sucesso!')
           return redirect('noticia:exibe_noticia',id=noticia.id)
    else:#requisicao do tipo get
        try:#caso em que o usuario foi alterar uma noticia e clicou em adicionar depois
            del request.session['noticia_id']
        except KeyError:
            pass
        noticia_form=NoticiaForm()
    return render(request,'noticia/cadastro_noticia.html',{'form':noticia_form})
def exibe_noticia(request,id):
    noticia=get_object_or_404(Noticia,pk=id)
    request.session['noticia_id_del']=id
    return render(request,'noticia/exibe_noticia.html',{'noticia':noticia})
def edita_noticia(request,id):
    noticia=get_object_or_404(Noticia,pk=id)
    noticia_form=NoticiaForm(instance=noticia)
    request.session['noticia_id']=id#chaves diferentes para evitar bugs
    return render(request,'noticia/cadastro_noticia.html',{'form':noticia_form})
def remove_noticia(request):
    noticia_id=request.session.get('noticia_id_del')
    noticia=get_object_or_404(Noticia,pk=noticia_id)#caso nao encontrado as proximas linhas nao serao executadas
    noticia.delete()
    del request.session['noticia_id_del']#deleta essa chave do objeto sessao
    messages.add_message(request,messages.INFO,'Noticia removida')
    return render(request,'noticia/exibe_noticia.html',{'noticia':noticia})