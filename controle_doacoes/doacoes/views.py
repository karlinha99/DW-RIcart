from django.shortcuts import render, get_object_or_404, redirect
from .models import Doador, Doacao
from .forms import DoadorForm, DoacaoForm



def index(request):
    return render(request, 'doacoes/index.html')

def doador_list(request):
    doadores = Doador.objects.all()
    return render(request, 'doacoes/doador_list.html', {'doadores': doadores})

def doador_detail(request, pk):
    doador = get_object_or_404(Doador, pk=pk)
    return render(request, 'doacoes/doador_detail.html', {'doador': doador})

def doador_create(request):
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doador_list')
    else:
        form = DoadorForm()
    return render(request, 'doacoes/doador_form.html', {'form': form})

def doador_update(request, pk):
    doador = get_object_or_404(Doador, pk=pk)
    if request.method == 'POST':
        form = DoadorForm(request.POST, instance=doador)
        if form.is_valid():
            form.save()
            return redirect('doador_list')
    else:
        form = DoadorForm(instance=doador)
    return render(request, 'doacoes/doador_form.html', {'form': form})

def doador_delete(request, pk):
    doador = get_object_or_404(Doador, pk=pk)
    if request.method == 'POST':
        doador.delete()
        return redirect('doador_list')
    return render(request, 'doacoes/doador_confirm_delete.html', {'doador': doador})

def doacao_list(request):
    doacoes = Doacao.objects.all()
    return render(request, 'doacoes/doacao_list.html', {'doacoes': doacoes})

def doacao_detail(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    return render(request, 'doacoes/doacao_detail.html', {'doacao': doacao})

def doacao_create(request):
    if request.method == 'POST':
        form = DoacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doacao_list')
    else:
        form = DoacaoForm()
    return render(request, 'doacoes/doacao_form.html', {'form': form})

def doacao_update(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    if request.method == 'POST':
        form = DoacaoForm(request.POST, instance=doacao)
        if form.is_valid():
            form.save()
            return redirect('doacao_list')
    else:
        form = DoacaoForm(instance=doacao)
    return render(request, 'doacoes/doacao_form.html', {'form': form})

def doacao_delete(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    if request.method == 'POST':
        doacao.delete()
        return redirect('doacao_list')
    return render(request, 'doacoes/doacao_confirm_delete.html', {'doacao': doacao})
