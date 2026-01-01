from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensagem
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def landpage(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        texto = request.POST.get('mensagem')

        if texto and len(texto) > 1000:
            return render(request, 'landpage.html', {
                'erro': 'A mensagem excedeu o limite de 1000 caracteres.'
            })

        # Validação: exigir pelo menos dois nomes (ex: 'João Silva')
        if not nome or len([p for p in nome.split() if p.strip()]) < 2:
            return render(request, 'landpage.html', {
                'erro_nome': 'Por favor, insira pelo menos dois nomes.'
            })

        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'landpage.html', {'erro_email': 'Por favor, insira um e-mail válido.'})

        Mensagem.objects.create(nome=nome, email=email, mensagem=texto)
        return render(request, 'landpage.html', {'sucesso': True})

    return render(request, 'landpage.html')


@login_required(login_url='login')
def painel_mensagens(request):
    mensagens = Mensagem.objects.all().order_by('-data_envio')
    return render(request, 'painel.html', {'mensagens': mensagens})