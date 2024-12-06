from django.db import models

from django.db import models

class Sala(models.Model):
    numero = models.IntegerField()  # Número da sala
    nome = models.CharField(max_length=100)  # Nome descritivo da sala
    area = models.CharField(max_length=50, choices=[('saude', 'Área da Saúde'), ('pavilhao', 'Pavilhão')])
    url = models.URLField(max_length=200, blank=True, null=True)  # Link do vídeo no YouTube

    def __str__(self):
        return f"Sala {self.numero} - {self.nome}"

