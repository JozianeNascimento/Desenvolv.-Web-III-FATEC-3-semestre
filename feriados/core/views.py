from logging import NullHandler
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from core.models  import FeriadoModel

def feriados(request):
    hoje = date.today()
    qs = FeriadoModel.objects.all()
    if qs.filter(dia=hoje.day,mes=hoje.month):
        feriado = qs.filter(dia=hoje.day,mes=hoje.month)
    else:
        feriado = 'Não é feriado'
    return render(request, 'feriados.html', {'feriado' : feriado})