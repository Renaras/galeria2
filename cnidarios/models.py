from django.db import models

class imagem(models.Model):

    path = models.CharField(max_length=200)
    
class titulo(models.Model):

    path = models.CharField(max_length=200)
    
class descricao(models.Model):

    path = models.TextField(max_length=200)
