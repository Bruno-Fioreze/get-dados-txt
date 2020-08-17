from django.db import models

# Create your models here.

class Arquivo(models.Model):
    comprador = models.CharField(max_length=50,null=True,blank=True)
    descricao = models.CharField(max_length=50,null=True,blank=True)
    precounitario = models.FloatField(default=0.00,null=True,blank=True)
    quantidade = models.IntegerField(null=True,blank=True)
    endereco = models.CharField(max_length=50,null=True,blank=True)
    fornecedor = models.CharField(max_length=50,null=True,blank=True)
