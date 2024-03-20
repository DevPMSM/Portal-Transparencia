from django.shortcuts import render, redirect
from .models import Informacoes

# Create your views here.
def home(request):
    dados = Informacoes.objects.all() #pegar todas os dados que estão no bdd
    return render(request, "index.html", {"dados": dados}) #retorna um template, envia as dados p o template
   
def salvar(request):
    nome = request.POST.get("nome")
    cpf = request.POST.get("cpf")
    relatorio = request.POST.get("relatorio")
    Informacoes.objects.create(nome=nome, cpf=cpf, relatorio=relatorio) #cria o novo dado no banco
    dados = Informacoes.objects.all() 
    return render(request, "index.html", {"dados": dados}) #envia lista atualizada de dados p o index
    
def relatorio(request, id):
    informacao = Informacoes.objects.get(id=id)
    return render(request, "relatorio.html", {"informacao": informacao})

def editar(request, id):
    dado = Informacoes.objects.get(id=id)
    return render(request, "update.html", {"dado": dado})

def update(request, id):
    vnome = request.POST.get("nome")
    vcpf = request.POST.get("cpf")
    dado = Informacoes.objects.get(id=id) #recupera o dado pelo id do banco
    dado.nome = vnome
    dado.cpf = vcpf
    dado.save()
    #return redirect('home')
    dados = Informacoes.objects.all() 
    return render(request, "index.html", {"dados": dados}) #envia lista atualizada de dados p o index
    

def delete(request, id):
    dado = Informacoes.objects.get(id=id)
    dado.delete()
    return redirect(home)