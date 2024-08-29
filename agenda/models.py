from django.db import models
from usuarioagendas.models import UsuarioSistema

class Telefonos(models.Model):
    numero = models.CharField(max_length=10)
    usuarioagenda = models.ForeignKey(UsuarioSistema,related_name='numeros',on_delete=models.CASCADE)

    class Meta:
        unique_together = ['numero', 'usuarioagenda']
    def __str__(self):
        return f" {self.numero} - {self.usuarioagenda}"

