from django.db import models

class UsuarioSistema(models.Model):
    usuario = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=15, unique=True, null=False, blank=False)

    def __str__(self):
        return f" {self.usuario} - {self.telefono}"

