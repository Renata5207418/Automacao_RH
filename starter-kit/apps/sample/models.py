from django.db import models
from django.core.validators import FileExtensionValidator
from django import forms
from django.db import models


class Vaga(models.Model):
    titulo = models.CharField(max_length=255)
    data_publicacao = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('aberta', 'Aberta'),
        ('fechada', 'Fechada')
    ], default='aberta')

    def __str__(self):
        return self.titulo


class Candidato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    vaga_interesse = models.CharField(max_length=255)
    curriculo = models.FileField(upload_to='curriculos/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'txt'])])
    observacoes = models.TextField(blank=True)
    processo_selecao = models.CharField(max_length=21, null=True, blank=True, choices=[
        ('entrevistado', 'Entrevistado'),
        ('aguardando_entrevista', 'Aguardando Entrevista'),
    ])
    resultado = models.CharField(
        max_length=50,
        choices=[
            ('aprovado', 'Aprovado'),
            ('reprovado', 'Reprovado'),
            ('futura', 'Vaga Futura'),
        ],
        blank=True,
        null=True,
    )
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True, default='static/images/default-avatar-new.png')

    def __str__(self):
        return self.nome
