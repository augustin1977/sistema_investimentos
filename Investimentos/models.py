from django.db import models
from djmoney.models.fields import *
from usuarios.models import *
from datetime import *

class tipo_investimento(models.Model):
    nome=models.CharField(max_length=50)
    ativo=models.BooleanField(default=True)
    def __str__(self):
        return self.nome
class banco(models.Model):
    nome=models.CharField(max_length=50)
    ativo=models.BooleanField(default=True)
    def __str__(self):
        return self.nome
class investimento(models.Model):
    nome=models.CharField(max_length=50)
    tipo=models.ForeignKey(tipo_investimento, on_delete=models.CASCADE)
    proprietario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    banco=models.ForeignKey(banco, on_delete=models.CASCADE)
    valor=MoneyField(max_digits=17, decimal_places=2, default_currency='BRL')
    data=models.DateField()
    ultima_atualizacao=models.DateTimeField(auto_now=True)
    ativo=models.BooleanField(default=True)
    
    class Meta:
        unique_together=["nome","proprietario","data","banco","valor","tipo"]
        
    def __str__(self):
        return f"Banco:{self.banco}-Data:{self.data}-Tipo:{self.tipo}-Nome:{self.nome}-Valor:{self.valor}"



