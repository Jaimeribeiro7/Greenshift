from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    revendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    valor_fatura = models.DecimalField(max_digits=10, decimal_places=2)
    fatura = models.FileField(upload_to='faturas/')
    documento = models.FileField(upload_to='documentos/')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Comissao(models.Model):
    revendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('disponivel', 'Disponível'),
        ('sacado', 'Sacado'),
    ])
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.revendedor.username} - R$ {self.valor}"
