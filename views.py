from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cliente, Comissao

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    clientes = Cliente.objects.filter(revendedor=request.user)
    total_comissao = sum(c.valor for c in Comissao.objects.filter(revendedor=request.user))
    saldo_disponivel = sum(c.valor for c in Comissao.objects.filter(revendedor=request.user, status='disponivel'))
    return render(request, 'dashboard.html', {
        'clientes': clientes.count(),
        'total_comissao': total_comissao,
        'saldo_disponivel': saldo_disponivel,
    })

@login_required
def clientes_view(request):
    clientes = Cliente.objects.filter(revendedor=request.user)
    return render(request, 'clientes.html', {'clientes': clientes})

@login_required
def financeiro_view(request):
    comissoes = Comissao.objects.filter(revendedor=request.user)
    return render(request, 'financeiro.html', {'comissoes': comissoes})

@login_required
def materiais_view(request):
    return render(request, 'materiais.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
