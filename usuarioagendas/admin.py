from django.contrib import admin

from usuarioagendas.models import UsuarioSistema

@admin.register(UsuarioSistema)
class UsuarioSistemaAdmin(admin.ModelAdmin):
   list_display = ['id','usuario']

