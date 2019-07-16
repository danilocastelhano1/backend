from django.db import models

class TODO(models.Model):
    conteudo = models.CharField(max_length=200)
    is_completo = models.CharField(max_length=3)