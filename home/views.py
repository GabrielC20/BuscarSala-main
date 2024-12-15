from django.shortcuts import redirect, render

from django.contrib.messages import constants
from django.contrib import messages

from usuario.models import AtivarPesquisaSalas, Contador, Sala,Curso,RegistroCurso

from django.urls import reverse
from django.contrib.auth import logout

import datetime


def home(request):
    status_pesquisa_salas = AtivarPesquisaSalas.objects.all().first().ativado
    
    return render(request,'menu.html',{"status_pesquisa_salas":status_pesquisa_salas})

def pesquisar_sala(request):
    cursos = Curso.objects.all()
    turnos = RegistroCurso.TURNO_CHOICES

    context = {
        'cursos': cursos,
        'turnos': turnos
    }

    if request.method == 'POST':
        semestre = request.POST['semestre']
        curso = request.POST['curso']
        turno = request.POST['turno']
        
        # Obtendo o dia da semana atual
        dia_semana = datetime.datetime.today().weekday()
        # Mapear para o formato do banco de dados (Django começa com 0 para segunda-feira)
        dias_mapping = {
            0: '2',  # Segunda-feira
            1: '3',  # Terça-feira
            2: '4',  # Quarta-feira
            3: '5',  # Quinta-feira
            4: '6',  # Sexta-feira
            5: '7',  # Sábado
            6: '1',  # Domingo
        }
        dia_atual = dias_mapping[dia_semana]
        
        try:
            # Filtrar RegistroCurso com base nos critérios
            registros = RegistroCurso.objects.filter(
                curso=curso,
                turno=turno,
                semestre=semestre
            )
            
            # Verificar o cronograma das salas para o dia atual
            for registro in registros:
                for cronograma in registro.sala.all():
                    if cronograma.dias.filter(dia=dia_atual).exists():
                        # Encontrou a sala no dia atual
                        return redirect(reverse('video_sala', kwargs={'id_sala': cronograma.sala.pk}))
            
            # Se nenhum registro corresponder ao dia atual
            messages.add_message(request, constants.ERROR, "Sala não encontrada para o dia atual")

        except RegistroCurso.DoesNotExist:
            messages.add_message(request, constants.ERROR, "Registro de curso não encontrado")
    
    return render(request, 'pesquisarSala.html', context)


def index (request):
    
    return render(request, 'index.html')

def video_sala (request,id_sala):
    sala = Sala.objects.get( pk = id_sala )
    
    try:
        Contador.objects.create(sala=sala)
    except:
        pass
    
    return render (request, 'videoSala.html',{"sala":sala})

def pavilhao(request, numero_pavilhao):
    # Mapeamento de nomes personalizados para cada pavilhão
    nomes_pavilhoes = {
        '1': "PAVILHÃO 01",
        '2': "PAVILHÃO 02",
        '3': "Área da Saúde",
    }
    
    # Garantir que o numero_pavilhao seja uma string para o zfill
    numero_pavilhao_str = str(numero_pavilhao)
    
    # Buscar o nome do pavilhão ou usar um padrão se não existir
    nome_pavilhao = nomes_pavilhoes.get(numero_pavilhao_str, f"PAVILHÃO {numero_pavilhao_str.zfill(2)}")

    # Buscar salas do pavilhão
    salas = Sala.objects.filter(pavilhao=numero_pavilhao_str)

    # Para cada sala, garantir que o nome personalizado seja o que está no banco de dados
    for sala in salas:
        # Se o nome personalizado estiver vazio, atribuímos um valor padrão
        if not sala.nome_personalizado:
            sala.nome_personalizado = f"Sala {sala.numero}"

    return render(request, 'pavilhao.html', {
        'salas': salas,
        'numero_pavilhao': numero_pavilhao_str,
        'nome_pavilhao': nome_pavilhao,
    })







def deslogar(request):
    logout(request)
    return redirect("/")