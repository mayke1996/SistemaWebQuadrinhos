from django.db import models


class info_quadrinhos(models.Model):

  titulo = models.CharField(
    max_length=255,
    null=False,
    blank=False
)
  descricao = models.CharField(
    max_length=500,
    null=False,
    blank=False
)
  serie = models.CharField(
    max_length=100,
    null=False,
    blank=False
)
  thumbnail = models.CharField(
    max_length=200,
    null=False,
    blank=False
)

class usuario(models.Model):

  nome = models.CharField(
    max_length=70,
    null=False,
    blank=False
)
  email = models.CharField(
    max_length=60,
    null=False,
    blank=False
)
  senha = models.CharField(
    max_length=80,
    null=False,
    blank=False
)
